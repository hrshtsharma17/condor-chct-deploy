git clone https://github.com/madgraph5/madgraph4gpu.git
cd madgraph4gpu
export MADGRAPH4GPU_HOME=`pwd`
cd epochX/cudacpp/gg_ttgg.sa/SubProcesses/P1_Sigma_sm_gg_ttxgg
sed -i 's/maxrregcount 128 /maxrregcount 160 /' makefile
echo Max Reg = 160
# sed -i 's/sudo//g' profile.sh
make cleanall
make AVX=avx2 FPTYPE=d HELINL=0
# ./check.exe -p 64 256 1
./gcheck.exe -p 108 256 6
# sh profile.sh -nogui -p 108 256 6
