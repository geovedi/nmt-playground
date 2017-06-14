```
root@xyz-01:/home/xyz/workdir/src/marian-3d6/build# cmake ..
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Found CUDA: /usr/local/cuda-8.0 (found version "8.0")
-- Compiling with CUDA support
-- Boost version: 1.58.0
-- Found the following Boost libraries:
--   system
--   filesystem
--   program_options
--   timer
--   iostreams
--   python
--   thread
--   chrono
--   regex
--   date_time
--   atomic
-- Looking for CL_VERSION_2_0
-- Looking for CL_VERSION_2_0 - not found
-- Looking for CL_VERSION_1_2
-- Looking for CL_VERSION_1_2 - found
-- Found OpenCL: /usr/lib/x86_64-linux-gnu/libOpenCL.so (found version "1.2")
-- Found PythonLibs: /usr/lib/x86_64-linux-gnu/libpython2.7.so (found suitable version "2.7.12", minimum required is "2.7")
-- Found Python
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.2.8")
-- Found Git: /usr/bin/git (found version "2.7.4")
-- Git version: e817534
-- Found SparseHash: /usr/include
-- Found CUDA: /usr/local/cuda-8.0 (found suitable version "8.0", minimum required is "8.0")
-- Boost version: 1.58.0
-- Found the following Boost libraries:
--   system
--   timer
--   iostreams
--   filesystem
--   chrono
--   program_options
--   thread
--   regex
--   date_time
--   atomic
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/xyz/workdir/src/marian-3d6/build

root@xyz-01:/home/xyz/workdir/src/marian-3d6/build# make -j8
Scanning dependencies of target atools
Scanning dependencies of target libyaml-cpp-amun
Scanning dependencies of target cpumode
Scanning dependencies of target libcommon
Scanning dependencies of target extract_lex
Scanning dependencies of target libcnpy
Scanning dependencies of target libyaml-cpp
Scanning dependencies of target fast_align
[  0%] Building CXX object src/amun/3rd_party/extract_lex/CMakeFiles/extract_lex.dir/extract-lex-main.cpp.o
[  1%] Building CXX object src/amun/3rd_party/CMakeFiles/libcnpy.dir/cnpy/cnpy.cpp.o
[  1%] Building CXX object src/amun/3rd_party/fast_align/CMakeFiles/fast_align.dir/src/fast_align.cc.o
[  1%] Building CXX object src/amun/3rd_party/fast_align/CMakeFiles/atools.dir/src/alignment_io.cc.o
[  2%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/regex_yaml.cpp.o
[  3%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/ostream_wrapper.cpp.o
[  3%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/git_version.cpp.o
[  5%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/base_matrix.cpp.o
[  6%] Building CXX object src/amun/CMakeFiles/cpumode.dir/cpu/mblas/matrix.cpp.o
[  6%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/convert.cpp.o
[  6%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/config.cpp.o
[  6%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/nodebuilder.cpp.o
[  7%] Building CXX object src/amun/3rd_party/fast_align/CMakeFiles/atools.dir/src/atools.cc.o
[  7%] Built target libcnpy
[  9%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/scanscalar.cpp.o
[ 10%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/emitfromevents.cpp.o
[ 10%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/scanner.cpp.o
[ 10%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/scantag.cpp.o
[ 11%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/parser.cpp.o
[ 11%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/stream.cpp.o
[ 11%] Linking CXX executable ../../../../atools
[ 11%] Built target atools
[ 12%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/convert.cpp.o
[ 12%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/directives.cpp.o
[ 14%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/singledocparser.cpp.o
[ 15%] Building CXX object src/amun/3rd_party/extract_lex/CMakeFiles/extract_lex.dir/utils.cpp.o
[ 15%] Building CXX object src/amun/3rd_party/extract_lex/CMakeFiles/extract_lex.dir/exception.cpp.o
[ 15%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/memory.cpp.o
[ 16%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/node.cpp.o
[ 18%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/regex_yaml.cpp.o
[ 18%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/exp.cpp.o
[ 19%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/emitter.cpp.o
[ 20%] Building CXX object src/amun/3rd_party/fast_align/CMakeFiles/fast_align.dir/src/ttables.cc.o
[ 20%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/emit.cpp.o
[ 22%] Linking CXX executable ../../../../extract_lex
[ 22%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/nodeevents.cpp.o
[ 23%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/null.cpp.o
[ 23%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/binary.cpp.o
[ 23%] Built target extract_lex
[ 24%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/emitfromevents.cpp.o
[ 24%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/scantoken.cpp.o
[ 25%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/emitterstate.cpp.o
[ 25%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/scantag.cpp.o
/home/xyz/workdir/src/marian-3d6/src/amun/3rd_party/fast_align/src/ttables.cc: In member function ‘void TTable::DeserializeLogProbsFromText(std::istream*, Dict&)’:
/home/xyz/workdir/src/marian-3d6/src/amun/3rd_party/fast_align/src/ttables.cc:20:12: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
     if (ie >= static_cast<int>(ttable.size())) ttable.resize(ie + 1);
            ^
[ 27%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/simplekey.cpp.o
[ 28%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/simplekey.cpp.o
[ 28%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/tag.cpp.o
[ 28%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/nodeevents.cpp.o
[ 29%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/tag.cpp.o
[ 31%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/emitterstate.cpp.o
[ 31%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/contrib/graphbuilderadapter.cpp.o
[ 32%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/contrib/graphbuilder.cpp.o
[ 32%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/node_data.cpp.o
[ 33%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/emitterutils.cpp.o
[ 33%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/binary.cpp.o
[ 33%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/parse.cpp.o
[ 35%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/emit.cpp.o
[ 36%] Building CXX object src/amun/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp-amun.dir/ostream_wrapper.cpp.o
[ 36%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/emitter.cpp.o
[ 37%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/emitterutils.cpp.o
[ 37%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/scantoken.cpp.o
[ 37%] Building CXX object src/amun/CMakeFiles/cpumode.dir/cpu/mblas/phoenix_functions.cpp.o
[ 38%] Building CXX object src/amun/CMakeFiles/cpumode.dir/cpu/dl4mt/decoder.cpp.o
[ 40%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/scanner.cpp.o
[ 40%] Building CXX object src/amun/CMakeFiles/cpumode.dir/cpu/dl4mt/encoder.cpp.o
[ 41%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/exception.cpp.o
[ 41%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/filter.cpp.o
[ 41%] Linking CXX executable ../../../../fast_align
[ 41%] Built target fast_align
[ 42%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/god.cpp.o
[ 42%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/exp.cpp.o
[ 44%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/directives.cpp.o
[ 44%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/nodebuilder.cpp.o
[ 45%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/memory.cpp.o
[ 45%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/parser.cpp.o
[ 45%] Built target libyaml-cpp-amun
[ 46%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/stream.cpp.o
[ 46%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/null.cpp.o
[ 48%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/singledocparser.cpp.o
[ 48%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/parse.cpp.o
[ 49%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/node.cpp.o
[ 49%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/exceptions.cpp.o
[ 50%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/scanscalar.cpp.o
[ 50%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/history.cpp.o
[ 50%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/node_data.cpp.o
[ 51%] Building CXX object src/amun/CMakeFiles/cpumode.dir/cpu/dl4mt/gru.cpp.o
[ 53%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/contrib/graphbuilder.cpp.o
[ 53%] Building CXX object src/marian/src/3rd_party/yaml-cpp/CMakeFiles/libyaml-cpp.dir/contrib/graphbuilderadapter.cpp.o
[ 53%] Building CXX object src/amun/CMakeFiles/cpumode.dir/cpu/dl4mt/model.cpp.o
[ 54%] Building CXX object src/amun/CMakeFiles/cpumode.dir/cpu/decoder/encoder_decoder.cpp.o
[ 54%] Built target libyaml-cpp
[ 55%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/translator/marian_generated_helpers.cu.o
[ 55%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/graph/marian_generated_expression_graph.cu.o
[ 55%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/best_hyps.cpp.o
[ 57%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/decoder.cpp.o
[ 57%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/encoder_decoder_loader.cpp.o
[ 58%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/hypothesis.cpp.o
[ 58%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/loader.cpp.o
[ 59%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/logging.cpp.o
[ 59%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/output_collector.cpp.o
[ 61%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/printer.cpp.o
[ 62%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/encoder_decoder_state.cpp.o
[ 62%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/encoder_decoder.cpp.o
[ 63%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/encoder.cpp.o
[ 63%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/processor/bpe.cpp.o
[ 63%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/matrix_functions.cpp.o
[ 64%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/matrix.cpp.o
[ 64%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/model.cpp.o
[ 66%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/nth_element.cpp.o
[ 66%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/npz_converter.cpp.o
[ 67%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/scorer.cpp.o
[ 68%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/kernel.cpp.o
[ 68%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/debug-devices.cpp.o
[ 70%] Building CXX object src/amun/CMakeFiles/cpumode.dir/fpga/hello_world.cpp.o
[ 70%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/search.cpp.o
[ 71%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/sentence.cpp.o
[ 71%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/sentences.cpp.o
[ 72%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/types.cpp.o
[ 72%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/utils.cpp.o
[ 74%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/vocab.cpp.o
[ 74%] Building CXX object src/amun/CMakeFiles/libcommon.dir/common/translation_task.cpp.o
[ 74%] Built target cpumode
[ 75%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/graph/marian_generated_expression_operators.cu.o
[ 75%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/graph/marian_generated_node.cu.o
[ 76%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/graph/marian_generated_node_operators.cu.o
[ 76%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/tensors/marian_generated_tensor.cu.o
[ 77%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/kernels/marian_generated_tensor_operators.cu.o
[ 77%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/kernels/marian_generated_dropout.cu.o
[ 77%] Built target libcommon
[ 79%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/common/amun_generated_loader_factory.cpp.o
[ 80%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/kernels/marian_generated_sparse.cu.o
[ 81%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/layers/marian_generated_rnn.cu.o
[ 81%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/layers/marian_generated_attention.cu.o
[ 81%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/optimizers/marian_generated_clippers.cu.o
[ 83%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/optimizers/marian_generated_optimizers.cu.o
[ 83%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/decoder/amun_generated_encoder_decoder_state.cu.o
[ 84%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/decoder/amun_generated_encoder_decoder.cu.o
[ 84%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian.dir/translator/marian_generated_nth_element.cu.o
[ 84%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/dl4mt/amun_generated_encoder.cu.o
[ 85%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/dl4mt/amun_generated_gru.cu.o
[ 85%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/mblas/amun_generated_matrix.cu.o
[ 87%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/mblas/amun_generated_matrix_functions.cu.o
[ 87%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/mblas/amun_generated_nth_element.cu.o
[ 88%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/amun_generated_npz_converter.cu.o
[ 88%] Building NVCC (Device) object src/amun/CMakeFiles/amun.dir/gpu/amun_generated_types-gpu.cu.o
/usr/local/cuda-8.0/include/thrust/detail/allocator/allocator_traits.inl(92): warning: calling a __host__ function from a __host__ __device__ function is not allowed
          detected during:
            instantiation of "thrust::detail::disable_if<thrust::detail::allocator_traits_detail::has_member_construct1<Alloc, T>::value, void>::type thrust::detail::allocator_traits_detail::construct(Alloc &, T *) [with Alloc=thrust::device_malloc_allocator<amunmt::GPU::NthOut>, T=amunmt::GPU::NthOut]"
(269): here
            instantiation of "void thrust::detail::allocator_traits<Alloc>::construct(thrust::detail::allocator_traits<Alloc>::allocator_type &, T *) [with Alloc=thrust::device_malloc_allocator<amunmt::GPU::NthOut>, T=amunmt::GPU::NthOut]"
/usr/local/cuda-8.0/include/thrust/detail/allocator/default_construct_range.inl(46): here
            instantiation of "void thrust::detail::allocator_traits_detail::construct1_via_allocator<Allocator>::operator()(T &) [with Allocator=thrust::device_malloc_allocator<amunmt::GPU::NthOut>, T=amunmt::GPU::NthOut]"
/usr/local/cuda-8.0/include/thrust/detail/function.h(60): here
            instantiation of "Result thrust::detail::wrapped_function<Function, Result>::operator()(const Argument &) const [with Function=thrust::detail::allocator_traits_detail::construct1_via_allocator<thrust::device_malloc_allocator<amunmt::GPU::NthOut>>, Result=void, Argument=thrust::device_reference<amunmt::GPU::NthOut>]"
/usr/local/cuda-8.0/include/thrust/system/cuda/detail/for_each.inl(57): here
            instantiation of "void thrust::system::cuda::detail::for_each_n_detail::for_each_kernel::operator()(thrust::system::cuda::detail::bulk_::parallel_group<thrust::system::cuda::detail::bulk_::concurrent_group<thrust::system::cuda::detail::bulk_::agent<1UL>, 0UL>, 0UL> &, Iterator, Function, Size) [with Iterator=thrust::device_ptr<amunmt::GPU::NthOut>, Function=thrust::detail::wrapped_function<thrust::detail::allocator_traits_detail::construct1_via_allocator<thrust::device_malloc_allocator<amunmt::GPU::NthOut>>, void>, Size=unsigned int]"
/usr/local/cuda-8.0/include/thrust/system/cuda/detail/bulk/detail/apply_from_tuple.hpp(71): here
            [ 12 instantiation contexts not shown ]
            instantiation of "thrust::detail::enable_if<thrust::detail::allocator_traits_detail::needs_default_construct_via_allocator<Allocator, thrust::detail::pointer_element<Pointer>::type>::value, void>::type thrust::detail::allocator_traits_detail::default_construct_range(Allocator &, Pointer, Size) [with Allocator=thrust::device_malloc_allocator<amunmt::GPU::NthOut>, Pointer=thrust::device_ptr<amunmt::GPU::NthOut>, Size=std::size_t]"
/usr/local/cuda-8.0/include/thrust/detail/allocator/default_construct_range.inl(105): here
            instantiation of "void thrust::detail::default_construct_range(Allocator &, Pointer, Size) [with Allocator=thrust::device_malloc_allocator<amunmt::GPU::NthOut>, Pointer=thrust::device_ptr<amunmt::GPU::NthOut>, Size=std::size_t]"
/usr/local/cuda-8.0/include/thrust/detail/contiguous_storage.inl(194): here
            instantiation of "void thrust::detail::contiguous_storage<T, Alloc>::default_construct_n(thrust::detail::contiguous_storage<T, Alloc>::iterator, thrust::detail::contiguous_storage<T, Alloc>::size_type) [with T=amunmt::GPU::NthOut, Alloc=thrust::device_malloc_allocator<amunmt::GPU::NthOut>]"
/usr/local/cuda-8.0/include/thrust/detail/vector_base.inl(763): here
            instantiation of "void thrust::detail::vector_base<T, Alloc>::append(thrust::detail::vector_base<T, Alloc>::size_type) [with T=amunmt::GPU::NthOut, Alloc=thrust::device_malloc_allocator<amunmt::GPU::NthOut>]"
/usr/local/cuda-8.0/include/thrust/detail/vector_base.inl(239): here
            instantiation of "void thrust::detail::vector_base<T, Alloc>::resize(thrust::detail::vector_base<T, Alloc>::size_type) [with T=amunmt::GPU::NthOut, Alloc=thrust::device_malloc_allocator<amunmt::GPU::NthOut>]"
/home/xyz/workdir/src/marian-3d6/src/amun/gpu/mblas/nth_element.cu(312): here
Scanning dependencies of target marian
[ 89%] Building CXX object src/marian/src/CMakeFiles/marian.dir/3rd_party/exception.cpp.o
[ 90%] Building CXX object src/marian/src/CMakeFiles/marian.dir/common/logging.cpp.o
[ 90%] Building CXX object src/marian/src/CMakeFiles/marian.dir/3rd_party/cnpy/cnpy.cpp.o
[ 90%] Building CXX object src/marian/src/CMakeFiles/marian.dir/common/utils.cpp.o
[ 90%] Building CXX object src/marian/src/CMakeFiles/marian.dir/3rd_party/svd/svd.cpp.o
[ 92%] Building CXX object src/marian/src/CMakeFiles/marian.dir/layers/param_initializers.cpp.o
[ 92%] Building CXX object src/marian/src/CMakeFiles/marian.dir/training/config.cpp.o
[ 93%] Building CXX object src/marian/src/CMakeFiles/marian.dir/translator/history.cpp.o
[ 93%] Building CXX object src/marian/src/CMakeFiles/marian.dir/translator/output_collector.cpp.o
[ 94%] Building CXX object src/marian/src/CMakeFiles/marian.dir/data/vocab.cpp.o
[ 94%] Building CXX object src/marian/src/CMakeFiles/marian.dir/data/corpus.cpp.o
Scanning dependencies of target amun
[ 94%] Building CXX object src/amun/CMakeFiles/amun.dir/common/decoder_main.cpp.o
[ 96%] Linking CXX static library ../../../libmarian.a
[ 96%] Built target marian
[ 96%] Building NVCC (Device) object src/marian/src/CMakeFiles/marian_train.dir/command/marian_train_generated_marian.cu.o
Scanning dependencies of target marian_translate
[ 96%] Building CXX object src/marian/src/CMakeFiles/marian_translate.dir/command/s2s_translator.cpp.o
[ 97%] Linking CXX executable ../../amun
[ 97%] Built target amun
[ 98%] Linking CXX executable ../../../s2s
[ 98%] Built target marian_translate
Scanning dependencies of target marian_train
[100%] Linking CXX executable ../../../marian
[100%] Built target marian_train
```


```
root@xyz-01:/home/xyz/workdir/src/marian-3d6/build# ls
amun  atools  CMakeCache.txt  CMakeFiles  cmake_install.cmake  extract_lex  fast_align  libmarian.a  Makefile  marian  s2s  src
```


```
xyz@xyz-01:~/workdir/nmt/data$ head valid.bpe.en | /home/xyz/workdir/src/marian-3d6/build/amun -c ../exp.better/model.en2id.npz.amun.yml --log-info 1 --log-progress 0 -b 5 --cpu-threads 0 --gpu-threads 1 --mini-batch 10 --maxi-batch 100
[Wed June 14 20:29:58 2017] (I) Options: allow-unk: false
beam-size: 5
cpu-threads: 0
devices: [0]
fpga-devices:
  - 0
fpga-threads: 0
gpu-threads: 1
log-info: true
log-progress: false
max-length: 500
maxi-batch: 100
mini-batch: 10
n-best: false
no-debpe: false
normalize: true
relative-paths: false
return-alignment: false
return-soft-alignment: false
scorers:
  F0:
    path: /home/xyz/workdir/nmt/exp.better/model.en2id.npz
    type: Nematus
show-weights: false
softmax-filter:
  []
source-vocab: /home/xyz/workdir/nmt/exp.better/vocab.en.json
target-vocab: /home/xyz/workdir/nmt/exp.better/vocab.id.json
weights:
  F0: 1
wipo: false

[Wed June 14 20:29:58 2017] (I) Loading scorers...
[Wed June 14 20:29:58 2017] (I) Loading model /home/xyz/workdir/nmt/exp.better/model.en2id.npz onto gpu 0
[Wed June 14 20:30:00 2017] (I) Reading from stdin
[Wed June 14 20:30:00 2017] (I) Setting GPU thread count to 1
[Wed June 14 20:30:00 2017] (I) Setting CPU thread count to 0
[Wed June 14 20:30:00 2017] (I) Setting FPGA thread count to 0
[Wed June 14 20:30:00 2017] (I) Total number of threads: 1
[Wed June 14 20:30:00 2017] (I) Reading input
EncoderDecoder
dan ternyata ￭, saya melakukan pekerjaan yang sangat bagus ￭.
dan kami pergi ke par￭ ent￭ ing mengharapkan hidup kita terlihat seperti ini ￭.
orang Italia di￭ gantikan oleh pelatih Portugal di Inter Milan pada 2008 ￭.
saya memenangkan World Yo￭ Y￭ o Con￭ test lagi di di￭ visi kinerja arti￭ sti￭ k ￭.
dan di Irak akhirnya ￭, kekerasan terus meningkat lagi ￭, dan negara tersebut belum membentuk pemerintahan empat bulan setelah pemilihan parlemen ter￭ akhirnya ￭.
dalam waktu dekat ￭, deal￭ er mobil baru akan dibuka di sini ￭.
saya tidak ingin belajar operasi ￭.
sebuah se￭ pot￭ ong kon￭ ten ￭, sebuah acara ￭, menyebabkan seseorang berbicara ￭.
"￭ Se￭ orang wanita iman ￭, ￭" "￭ seorang ahli ￭, ￭" mungkin bahkan "￭ saudara perempuan ￭" ￭?
semakin banyak ￭, kita menggunakan perangkat mobile ￭, dan kita ber￭ inter￭ aksi saat pergi ￭.
~EncoderDecoder
[Wed June 14 20:30:00 2017] (I) Total time:  0.131647s wall, 0.100000s user + 0.030000s system = 0.130000s CPU (98.7%)
```


```
xyz@xyz-01:~/workdir/nmt/data$ head valid.bpe.en | /home/xyz/workdir/src/marian-3d6/build/amun -c ../exp.better/model.en2id.npz.amun.yml --log-info 1 --log-progress 0 -b 5 --cpu-threads 8 --gpu-threads 0 --mini-batch 10 --maxi-batch 100
[Wed June 14 20:30:45 2017] (I) Options: allow-unk: false
beam-size: 5
cpu-threads: 8
devices: [0]
fpga-devices:
  - 0
fpga-threads: 0
gpu-threads: 0
log-info: true
log-progress: false
max-length: 500
maxi-batch: 100
mini-batch: 10
n-best: false
no-debpe: false
normalize: true
relative-paths: false
return-alignment: false
return-soft-alignment: false
scorers:
  F0:
    path: /home/xyz/workdir/nmt/exp.better/model.en2id.npz
    type: Nematus
show-weights: false
softmax-filter:
  []
source-vocab: /home/xyz/workdir/nmt/exp.better/vocab.en.json
target-vocab: /home/xyz/workdir/nmt/exp.better/vocab.id.json
weights:
  F0: 1
wipo: false

[Wed June 14 20:30:45 2017] (I) Loading scorers...
[Wed June 14 20:30:45 2017] (I) Loading model /home/xyz/workdir/nmt/exp.better/model.en2id.npz
[Wed June 14 20:30:45 2017] (I) Reading from stdin
[Wed June 14 20:30:45 2017] (I) Setting GPU thread count to 0
[Wed June 14 20:30:45 2017] (I) Setting CPU thread count to 8
[Wed June 14 20:30:45 2017] (I) Setting FPGA thread count to 0
[Wed June 14 20:30:45 2017] (I) Total number of threads: 8
[Wed June 14 20:30:45 2017] (I) Reading input
Segmentation fault (core dumped)
```
