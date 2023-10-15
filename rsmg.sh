MAX_REG_COUNT=256
BLOCK_NUMBER=108
EPOCHS=6

echo "MAX_REG_COUNT = $MAX_REG_COUNT, Block Number = $BLOCK_NUMBER, EPOCHS = $EPOCHS"
git clone https://github.com/madgraph5/madgraph4gpu.git
cd madgraph4gpu
export MADGRAPH4GPU_HOME=`pwd`
cd epochX/cudacpp/gg_ttgg.sa/SubProcesses/P1_Sigma_sm_gg_ttxgg
sed -i "s/maxrregcount 128 /maxrregcount $MAX_REG_COUNT /" makefile
echo "Max Reg = $MAX_REG_COUNT"
# sed -i 's/sudo//g' profile.sh
make cleanall
make AVX=avx2 FPTYPE=d HELINL=0
./gcheck.exe -p $BLOCK_NUMBER $MAX_REG_COUNT $EPOCHS
