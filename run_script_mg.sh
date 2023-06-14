git clone https://github.com/madgraph5/madgraph4gpu.git
cd madgraph4gpu
export MADGRAPH4GPU_HOME=`pwd`
cd epochX/cudacpp/gg_ttgg.sa/SubProcesses/P1_Sigma_sm_gg_ttxgg
make cleanall
make AVX=avx2 FPTYPE=d HELINL=0
./check.exe -p 64 256 1
./gcheck.exe -p 64 256 1
