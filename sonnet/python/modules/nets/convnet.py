# Copyright 2017 The Sonnet Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""A minimal interface convolutional networks module."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import functools

from six.moves import xrange  # pylint: disable=redefined-builtin
from sonnet.python.modules import base
from sonnet.python.modules import batch_norm
from sonnet.python.modules import conv
from sonnet.python.modules import util

import tensorflow as tf

DATA_FORMAT_NCHW = "NCHW"
DATA_FORMAT_NHWC = "NHWC"
SUPPORTED_2D_DATA_FORMATS = {DATA_FORMAT_NCHW, DATA_FORMAT_NHWC}


def _replicate_elements(input_iterable, num_times):
    """Replicates entry in `input_iterable` if `input_iterable` is of length 1."""
    if len(input_iterable) == 1:
        return (input_iterable[0],) * num_times
    return tuple(input_iterable)


class ConvNet2D(base.AbstractModule, base.Transposable):
    """A 2D Convolutional Network module."""

    POSSIBLE_INITIALIZER_KEYS = {"w", "b"}
    # Keep old name for backwards compatibility

    POSSIBLE_KEYS = POSSIBLE_INITIALIZER_KEYS

    def __init__(
        self,
        output_channels,
        kernel_shapes,
        strides,
        paddings,
        rates=(1,),
        activation=tf.nn.relu,
        activate_final=False,
        initializers=None,
        partitioners=None,
        regularizers=None,
        use_batch_norm=False,
        use_bias=True,
        batch_norm_config=None,
        data_format=DATA_FORMAT_NHWC,
        custom_getter=None,
        name="conv_net_2d",
    ):
        """Constructs a `ConvNet2D` module.

        By default, neither batch normalization nor activation are applied to the
        output of the final layer.

        Args:
          output_channels: Iterable of output channels, as defined in
            `conv.Conv2D`. Output channels can be defined either as number or via a
            callable. In the latter case, since the function invocation is deferred
            to graph construction time, the user must only ensure that entries can
            be called when build is called. Each entry in the iterable defines
            properties in the corresponding convolutional layer.
          kernel_shapes: Iterable of kernel sizes as defined in `conv.Conv2D`; if
            the list contains one element only, the same kernel shape is used in
            each layer of the network.
          strides: Iterable of kernel strides as defined in `conv.Conv2D`; if the
            list contains one element only, the same stride is used in each layer of
            the network.
          paddings: Iterable of padding options, either `snt.SAME` or
            `snt.VALID`; if the Iterable contains one element only, the same padding
            is used in each layer of the network.
          rates: Iterable of dilation rates as defined in `conv.Conv2D`; if the
            list contains one element only, the same rate is used in each layer of
            the network.
          activation: An activation op.
          activate_final: Boolean determining if the activation and batch
            normalization, if turned on, are applied to the final layer.
          initializers: Optional dict containing ops to initialize the filters of
            the whole network (with key 'w') or biases (with key 'b').
          partitioners: Optional dict containing partitioners to partition
              weights (with key 'w') or biases (with key 'b'). As a default, no
              partitioners are used.
          regularizers: Optional dict containing regularizers for the filters of the
            whole network (with key 'w') or biases (with key 'b'). As a default, no
            regularizers are used. A regularizer should be a function that takes a
            single `Tensor` as an input and returns a scalar `Tensor` output, e.g.
            the L1 and L2 regularizers in `tf.contrib.layers`.
          use_batch_norm: Boolean determining if batch normalization is applied
            after convolution.
          use_bias: Boolean or iterable of booleans determining whether to include
            bias parameters in the convolutional layers. Default `True`.
          batch_norm_config: Optional mapping of additional configuration for the
            `snt.BatchNorm` modules.
          data_format: A string, one of "NCHW" or "NHWC". Specifies whether the
            channel dimension of the input and output is the last dimension
            (default, "NHWC"), or the second dimension ("NCHW").
          custom_getter: Callable or dictionary of callables to use as
              custom getters inside the module. If a dictionary, the keys
              correspond to regexes to match variable names. See the
              `tf.get_variable` documentation for information about the
              custom_getter API.
          name: Name of the module.

        Raises:
          TypeError: If `output_channels` is not iterable; or if `kernel_shapes` is
            not iterable; or `strides` is not iterable; or `paddings` is not
            iterable; or if `activation` is not callable.
          ValueError: If `output_channels` is empty; or if `kernel_shapes` has not
            length 1 or `len(output_channels)`; or if `strides` has not
            length 1 or `len(output_channels)`; or if `paddings` has not
            length 1 or `len(output_channels)`; or if `rates` has not
            length 1 or `len(output_channels)`; or if the given data_format is not a
            supported format ("NHWC" or "NCHW").
          KeyError: If `initializers`, `partitioners` or `regularizers` contain any
            keys other than 'w' or 'b'.
          TypeError: If any of the given initializers, partitioners or regularizers
            are not callable.
        """
        if not isinstance(output_channels, collections.Iterable):
            raise TypeError("output_channels must be iterable")
        output_channels = tuple(output_channels)

        if not isinstance(kernel_shapes, collections.Iterable):
            raise TypeError("kernel_shapes must be iterable")
        kernel_shapes = tuple(kernel_shapes)

        if not isinstance(strides, collections.Iterable):
            raise TypeError("strides must be iterable")
        strides = tuple(strides)

        if not isinstance(paddings, collections.Iterable):
            raise TypeError("paddings must be iterable")
        paddings = tuple(paddings)

        if not isinstance(rates, collections.Iterable):
            raise TypeError("rates must be iterable")
        rates = tuple(rates)

        super(ConvNet2D, self).__init__(name=name, custom_getter=custom_getter)

        if not output_channels:
            raise ValueError("output_channels must not be empty")
        self._output_channels = tuple(output_channels)
        self._num_layers = len(self._output_channels)

        self._input_shape = None

        if data_format not in SUPPORTED_2D_DATA_FORMATS:
            raise ValueError(
                "Invalid data_format {}. Allowed formats " "{}".format(data_format, SUPPORTED_2D_DATA_FORMATS)
            )
        self._data_format = data_format

        self._initializers = util.check_initializers(initializers, self.POSSIBLE_INITIALIZER_KEYS)
        self._partitioners = util.check_partitioners(partitioners, self.POSSIBLE_INITIALIZER_KEYS)
        self._regularizers = util.check_regularizers(regularizers, self.POSSIBLE_INITIALIZER_KEYS)

        if not callable(activation):
            raise TypeError("Input 'activation' must be callable")
        self._activation = activation
        self._activate_final = activate_final

        self._kernel_shapes = _replicate_elements(kernel_shapes, self._num_layers)
        if len(self._kernel_shapes) != self._num_layers:
            raise ValueError("kernel_shapes must be of length 1 or len(output_channels)")

        self._strides = _replicate_elements(strides, self._num_layers)
        if len(self._strides) != self._num_layers:
            raise ValueError("""strides must be of length 1 or len(output_channels)""")

        self._paddings = _replicate_elements(paddings, self._num_layers)
        if len(self._paddings) != self._num_layers:
            raise ValueError("""paddings must be of length 1 or len(output_channels)""")

        self._rates = _replicate_elements(rates, self._num_layers)
        if len(self._rates) != self._num_layers:
            raise ValueError("""rates must be of length 1 or len(output_channels)""")

        self._use_batch_norm = use_batch_norm

        self._batch_norm_config = batch_norm_config or {}

        if isinstance(use_bias, bool):
            use_bias = (use_bias,)
        else:
            if not isinstance(use_bias, collections.Iterable):
                raise TypeError("use_bias must be either a bool or an iterable")
            use_bias = tuple(use_bias)
        self._use_bias = _replicate_elements(use_bias, self._num_layers)

        self._instantiate_layers()

    def _instantiate_layers(self):
        """Instantiates all the convolutional modules used in the network."""

        with self._enter_variable_scope():
            self._layers = tuple(
                conv.Conv2D(
                    name="conv_2d_{}".format(i),
                    output_channels=self._output_channels[i],
                    kernel_shape=self._kernel_shapes[i],
                    stride=self._strides[i],
                    rate=self._rates[i],
                    padding=self._paddings[i],
                    use_bias=self._use_bias[i],
                    initializers=self._initializers,
                    partitioners=self._partitioners,
                    regularizers=self._regularizers,
                    data_format=self._data_format,
                )
                for i in xrange(self._num_layers)
            )

    def _build(self, inputs, is_training=None, test_local_stats=True):
        """Assembles the `ConvNet2D` and connects it to the graph.

        Args:
          inputs: A 4D Tensor of shape `[batch_size, input_height, input_width,
            input_channels]`.
          is_training: Boolean to indicate to `snt.BatchNorm` if we are
            currently training. Must be specified explicitly if `use_batchnorm` is
            `True`.
          test_local_stats: Boolean to indicate to `snt.BatchNorm` if batch
            normalization should  use local batch statistics at test time.
            By default `True`.

        Returns:
          A 4D Tensor of shape `[batch_size, output_height, output_width,
            output_channels[-1]]`.

        Raises:
          ValueError: If `is_training` is not explicitly specified when using
            batch normalization.
        """
        if self._use_batch_norm and is_training is None:
            raise ValueError("Boolean is_training flag must be explicitly specified " "when using batch normalization.")

        self._input_shape = tuple(inputs.get_shape().as_list())
        net = inputs

        final_index = len(self._layers) - 1
        for i, layer in enumerate(self._layers):
            net = layer(net)

            if i != final_index or self._activate_final:
                if self._use_batch_norm:
                    bn = batch_norm.BatchNorm(
                        name="batch_norm_{}".format(i),
                        **self._batch_norm_config,
                    )
                    net = bn(
                        net,
                        is_training=is_training,
                        test_local_stats=test_local_stats,
                    )

                net = self._activation(net)

        return net

    @property
    def layers(self):
        """Returns a tuple containing the convolutional layers of the network."""
        return self._layers

    @property
    def initializers(self):
        return self._initializers

    @property
    def partitioners(self):
        return self._partitioners

    @property
    def regularizers(self):
        return self._regularizers

    @property
    def strides(self):
        return self._strides

    @property
    def paddings(self):
        return self._paddings

    @property
    def rates(self):
        return self._rates

    @property
    def kernel_shapes(self):
        return self._kernel_shapes

    @property
    def output_channels(self):
        return tuple([x() if callable(x) else x for x in self._output_channels])

    @property
    def use_bias(self):
        return self._use_bias

    @property
    def use_batch_norm(self):
        return self._use_batch_norm

    @property
    def batch_norm_config(self):
        return self._batch_norm_config

    @property
    def activation(self):
        return self._activation

    @property
    def activate_final(self):
        return self._activate_final

    # Implements Transposable interface.
    @property
    def input_shape(self):
        """Returns shape of input `Tensor` passed at last call to `build`."""
        self._ensure_is_connected()
        return self._input_shape

    def _transpose(
        self,
        transpose_constructor,
        name=None,
        output_channels=None,
        kernel_shapes=None,
        strides=None,
        paddings=None,
        activation=None,
        activate_final=None,
        initializers=None,
        partitioners=None,
        regularizers=None,
        use_batch_norm=None,
        use_bias=None,
        batch_norm_config=None,
        data_format=None,
    ):
        """Returns transposed version of this network.

        Args:
          transpose_constructor: A method that creates an instance of the transposed
            network type. The method must accept the same kwargs as this methods
            with the exception of the `transpose_constructor` argument.
          name: Optional string specifying the name of the transposed module. The
            default name is constructed by appending "_transpose"
            to `self.module_name`.
          output_channels: Optional iterable of numbers of output channels.
          kernel_shapes: Optional iterable of kernel sizes. The default value is
            constructed by reversing `self.kernel_shapes`.
          strides: Optional iterable of kernel strides. The default value is
            constructed by reversing `self.strides`.
          paddings: Optional iterable of padding options, either `snt.SAME` or
            `snt.VALID`; The default value is constructed by reversing
            `self.paddings`.
          activation: Optional activation op. Default value is `self.activation`.
          activate_final: Optional boolean determining if the activation and batch
            normalization, if turned on, are applied to the final layer.
          initializers: Optional dict containing ops to initialize the filters of
            the whole network (with key 'w') or biases (with key 'b'). The default
            value is `self.initializers`.
          partitioners: Optional dict containing partitioners to partition
            weights (with key 'w') or biases (with key 'b'). The default value is
            `self.partitioners`.
          regularizers: Optional dict containing regularizers for the filters of the
            whole network (with key 'w') or biases (with key 'b'). The default is
            `self.regularizers`.
          use_batch_norm: Optional boolean determining if batch normalization is
            applied after convolution. The default value is `self.use_batch_norm`.
          use_bias: Optional boolean or iterable of booleans determining whether to
            include bias parameters in the convolutional layers. Default
            is constructed by reversing `self.use_bias`.
          batch_norm_config: Optional mapping of additional configuration for the
            `snt.BatchNorm` modules. Default is `self.batch_norm_config`.
          data_format: Optional string, one of "NCHW" or "NHWC". Specifies whether
            the channel dimension of the input and output is the last dimension.
            Default is `self._data_format`.
        Returns:
          Matching transposed module.

        Raises:
          ValueError: If output_channels is specified and its length does not match
            the number of layers.
        """

        if data_format is None:
            data_format = self._data_format

        if output_channels is None:
            output_channels = []
            channel_dim = -1 if data_format == DATA_FORMAT_NHWC else 1
            for layer in reversed(self._layers):
                output_channels.append(lambda l=layer: l.input_shape[channel_dim])

        elif len(output_channels) != len(self._layers):
            # Note that we only have to do this check for the output channels. Any
            # other inconsistencies will be picked up by ConvNet2D.__init__.
            raise ValueError(
                "Iterable output_channels length must match the "
                "number of layers ({}), but is {} instead.".format(len(self._layers), len(output_channels))
            )

        if kernel_shapes is None:
            kernel_shapes = reversed(self.kernel_shapes)

        if strides is None:
            strides = reversed(self.strides)

        if paddings is None:
            paddings = reversed(self.paddings)

        if activation is None:
            activation = self.activation

        if activate_final is None:
            activate_final = self.activate_final

        if initializers is None:
            initializers = self.initializers

        if partitioners is None:
            partitioners = self.partitioners

        if regularizers is None:
            regularizers = self.regularizers

        if use_batch_norm is None:
            use_batch_norm = self.use_batch_norm

        if use_bias is None:
            use_bias = reversed(self.use_bias)

        if batch_norm_config is None:
            batch_norm_config = self.batch_norm_config

        if name is None:
            name = self.module_name + "_transpose"

        return transpose_constructor(
            output_channels=output_channels,
            kernel_shapes=kernel_shapes,
            strides=strides,
            paddings=paddings,
            activation=activation,
            activate_final=activate_final,
            initializers=initializers,
            partitioners=partitioners,
            regularizers=regularizers,
            use_batch_norm=use_batch_norm,
            use_bias=use_bias,
            batch_norm_config=batch_norm_config,
            data_format=data_format,
            name=name,
        )

    # Implements Transposable interface.
    def transpose(
        self,
        name=None,
        output_channels=None,
        kernel_shapes=None,
        strides=None,
        paddings=None,
        activation=None,
        activate_final=None,
        initializers=None,
        partitioners=None,
        regularizers=None,
        use_batch_norm=None,
        use_bias=None,
        batch_norm_config=None,
        data_format=None,
    ):
        """Returns transposed version of this network.

        Args:
          name: Optional string specifying the name of the transposed module. The
            default name is constructed by appending "_transpose"
            to `self.module_name`.
          output_channels: Optional iterable of numbers of output channels.
          kernel_shapes: Optional iterable of kernel sizes. The default value is
            constructed by reversing `self.kernel_shapes`.
          strides: Optional iterable of kernel strides. The default value is
            constructed by reversing `self.strides`.
          paddings: Optional iterable of padding options, either `snt.SAME` or
            `snt.VALID`; The default value is constructed by reversing
            `self.paddings`.
          activation: Optional activation op. Default value is `self.activation`.
          activate_final: Optional boolean determining if the activation and batch
            normalization, if turned on, are applied to the final layer.
          initializers: Optional dict containing ops to initialize the filters of
            the whole network (with key 'w') or biases (with key 'b'). The default
            value is `self.initializers`.
          partitioners: Optional dict containing partitioners to partition
            weights (with key 'w') or biases (with key 'b'). The default value is
            `self.partitioners`.
          regularizers: Optional dict containing regularizers for the filters of the
            whole network (with key 'w') or biases (with key 'b'). The default is
            `self.regularizers`.
          use_batch_norm: Optional boolean determining if batch normalization is
            applied after convolution. The default value is `self.use_batch_norm`.
          use_bias: Optional boolean or iterable of booleans determining whether to
            include bias parameters in the convolutional layers. Default
            is constructed by reversing `self.use_bias`.
          batch_norm_config: Optional mapping of additional configuration for the
            `snt.BatchNorm` modules. Default is `self.batch_norm_config`.
          data_format: Optional string, one of "NCHW" or "NHWC". Specifies whether
            the channel dimension of the input and output is the last dimension.
            Default is `self._data_format`.

        Returns:
          Matching `ConvNet2DTranspose` module.

        Raises:
          ValueError: If output_channels is specified and its length does not match
            the number of layers.
          ValueError: If the given data_format is not a supported format ("NHWC" or
            "NCHW").
          NotImplementedError: If the convolutions are dilated.
        """
        for rate in self._rates:
            if rate != 1:
                raise NotImplementedError("Transpose dilated convolutions " "are not supported")
        output_shapes = []
        if data_format is None:
            data_format = self._data_format
        if data_format == DATA_FORMAT_NHWC:
            start_dim, end_dim = 1, -1
        elif data_format == DATA_FORMAT_NCHW:
            start_dim, end_dim = 2, 4
        else:
            raise ValueError(
                "Invalid data_format {:s}. Allowed formats " "{}".format(data_format, SUPPORTED_2D_DATA_FORMATS)
            )

        for layer in reversed(self._layers):
            output_shapes.append(lambda l=layer: l.input_shape[start_dim:end_dim])
        transpose_constructor = functools.partial(ConvNet2DTranspose, output_shapes=output_shapes)

        return self._transpose(
            transpose_constructor=transpose_constructor,
            name=name,
            output_channels=output_channels,
            kernel_shapes=kernel_shapes,
            strides=strides,
            paddings=paddings,
            activation=activation,
            activate_final=activate_final,
            initializers=initializers,
            partitioners=partitioners,
            regularizers=regularizers,
            use_batch_norm=use_batch_norm,
            use_bias=use_bias,
            batch_norm_config=batch_norm_config,
            data_format=data_format,
        )


class ConvNet2DTranspose(ConvNet2D):
    """A 2D Transpose-Convolutional Network module."""

    def __init__(
        self,
        output_channels,
        output_shapes,
        kernel_shapes,
        strides,
        paddings,
        activation=tf.nn.relu,
        activate_final=False,
        initializers=None,
        partitioners=None,
        regularizers=None,
        use_batch_norm=False,
        use_bias=True,
        batch_norm_config=None,
        data_format=DATA_FORMAT_NHWC,
        name="conv_net_2d_transpose",
    ):
        """Constructs a `ConvNetTranspose2D` module.

        `output_{shapes,channels}` can be defined either as iterable of
        {iterables,integers} or via a callable. In the latter case, since the
        function invocation is deferred to graph construction time, the user
        must only ensure that entries can be called returning meaningful values when
        build is called. Each entry in the iterable defines properties in the
        corresponding convolutional layer.

        By default, neither batch normalization nor activation are applied to the
        output of the final layer.

        Args:
          output_channels: Iterable of numbers of output channels.
          output_shapes: Iterable of output shapes as defined in
            `conv.conv2DTranpose`; if the iterable contains one element only, the
            same shape is used in each layer of the network.
          kernel_shapes: Iterable of kernel sizes as defined in `conv.Conv2D`; if
            the list contains one element only, the same kernel shape is used in
            each layer of the network.
          strides: Iterable of kernel strides as defined in `conv.Conv2D`; if the
            list contains one element only, the same stride is used in each layer of
            the network.
          paddings: Iterable of padding options, either `snt.SAME` or
            `snt.VALID`; if the Iterable contains one element only, the same padding
            is used in each layer of the network.
          activation: An activation op.
          activate_final: Boolean determining if the activation and batch
            normalization, if turned on, are applied to the final layer.
          initializers: Optional dict containing ops to initialize the filters of
            the whole network (with key 'w') or biases (with key 'b').
          partitioners: Optional dict containing partitioners to partition
              weights (with key 'w') or biases (with key 'b'). As a default, no
              partitioners are used.
          regularizers: Optional dict containing regularizers for the filters of the
            whole network (with key 'w') or biases (with key 'b'). As a default, no
            regularizers are used. A regularizer should be a function that takes a
            single `Tensor` as an input and returns a scalar `Tensor` output, e.g.
            the L1 and L2 regularizers in `tf.contrib.layers`.
          use_batch_norm: Boolean determining if batch normalization is applied
            after convolution.
          use_bias: Boolean or iterable of booleans determining whether to include
            bias parameters in the convolutional layers. Default `True`.
          batch_norm_config: Optional mapping of additional configuration for the
            `snt.BatchNorm` modules.
          data_format: A string, one of "NCHW" or "NHWC". Specifies whether the
            channel dimension of the input and output is the last dimension
            (default, "NHWC"), or the second dimension ("NCHW").
          name: Name of the module.

        Raises:
          TypeError: If `output_channels` is not iterable; or if `output_shapes`
            is not iterable; or if `kernel_shapes` is not iterable; or if `strides`
            is not iterable; or if `paddings` is not iterable; or if `activation` is
            not callable.
          ValueError: If `output_channels` is empty; or if `kernel_shapes` has not
            length 1 or `len(output_channels)`; or if `strides` has not
            length 1 or `len(output_channels)`; or if `paddings` has not
            length 1 or `len(output_channels)`.
          ValueError: If the given data_format is not a supported format ("NHWC" or
            "NCHW").
          KeyError: If `initializers`, `partitioners` or `regularizers` contain any
            keys other than 'w' or 'b'.
          TypeError: If any of the given initializers, partitioners or regularizers
            are not callable.
        """
        if not isinstance(output_channels, collections.Iterable):
            raise TypeError("output_channels must be iterable")
        output_channels = tuple(output_channels)
        num_layers = len(output_channels)

        if not isinstance(output_shapes, collections.Iterable):
            raise TypeError("output_shapes must be iterable")
        output_shapes = tuple(output_shapes)

        self._output_shapes = _replicate_elements(output_shapes, num_layers)
        if len(self._output_shapes) != num_layers:
            raise ValueError("output_shapes must be of length 1 or len(output_channels)")

        super(ConvNet2DTranspose, self).__init__(
            output_channels,
            kernel_shapes,
            strides,
            paddings,
            activation=activation,
            activate_final=activate_final,
            initializers=initializers,
            partitioners=partitioners,
            regularizers=regularizers,
            use_batch_norm=use_batch_norm,
            use_bias=use_bias,
            batch_norm_config=batch_norm_config,
            data_format=data_format,
            name=name,
        )

    def _instantiate_layers(self):
        """Instantiates all the convolutional modules used in the network."""

        with self._enter_variable_scope():
            self._layers = tuple(
                conv.Conv2DTranspose(
                    name="conv_2d_transpose_{}".format(i),
                    output_channels=self._output_channels[i],
                    output_shape=self._output_shapes[i],
                    kernel_shape=self._kernel_shapes[i],
                    stride=self._strides[i],
                    padding=self._paddings[i],
                    initializers=self._initializers,
                    partitioners=self._partitioners,
                    regularizers=self._regularizers,
                    data_format=self._data_format,
                    use_bias=self._use_bias[i],
                )
                for i in xrange(self._num_layers)
            )

    @property
    def output_shapes(self):
        return tuple([x() if callable(x) else x for x in self._output_shapes])

    # Implements Transposable interface.
    def transpose(
        self,
        name=None,
        output_channels=None,
        kernel_shapes=None,
        strides=None,
        paddings=None,
        activation=None,
        activate_final=None,
        initializers=None,
        partitioners=None,
        regularizers=None,
        use_batch_norm=None,
        use_bias=None,
        batch_norm_config=None,
        data_format=None,
    ):
        """Returns transposed version of this network.

        Args:
          name: Optional string specifying the name of the transposed module. The
            default name is constructed by appending "_transpose"
            to `self.module_name`.
          output_channels: Optional iterable of numbers of output channels.
          kernel_shapes: Optional iterable of kernel sizes. The default value is
            constructed by reversing `self.kernel_shapes`.
          strides: Optional iterable of kernel strides. The default value is
            constructed by reversing `self.strides`.
          paddings: Optional iterable of padding options, either `snt.SAME` or
            `snt.VALID`; The default value is constructed by reversing
            `self.paddings`.
          activation: Optional activation op. Default value is `self.activation`.
          activate_final: Optional boolean determining if the activation and batch
            normalization, if turned on, are applied to the final layer.
          initializers: Optional dict containing ops to initialize the filters of
            the whole network (with key 'w') or biases (with key 'b'). The default
            value is `self.initializers`.
          partitioners: Optional dict containing partitioners to partition
            weights (with key 'w') or biases (with key 'b'). The default value is
            `self.partitioners`.
          regularizers: Optional dict containing regularizers for the filters of the
            whole network (with key 'w') or biases (with key 'b'). The default is
            `self.regularizers`.
          use_batch_norm: Optional boolean determining if batch normalization is
            applied after convolution. The default value is `self.use_batch_norm`.
          use_bias: Optional boolean or iterable of booleans determining whether to
            include bias parameters in the convolutional layers. Default
            is constructed by reversing `self.use_bias`.
          batch_norm_config: Optional mapping of additional configuration for the
            `snt.BatchNorm` modules. Default is `self.batch_norm_config`.
          data_format: Optional string, one of "NCHW" or "NHWC". Specifies whether
            the channel dimension of the input and output is the last dimension.
            Default is `self._data_format`.

        Returns:
          Matching `ConvNet2D` module.

        Raises:
          ValueError: If output_channels is specified and its length does not match
            the number of layers.
        """
        return self._transpose(
            transpose_constructor=ConvNet2D,
            name=name,
            output_channels=output_channels,
            kernel_shapes=kernel_shapes,
            strides=strides,
            paddings=paddings,
            activation=activation,
            activate_final=activate_final,
            initializers=initializers,
            partitioners=partitioners,
            regularizers=regularizers,
            use_batch_norm=use_batch_norm,
            use_bias=use_bias,
            batch_norm_config=batch_norm_config,
            data_format=data_format,
        )
