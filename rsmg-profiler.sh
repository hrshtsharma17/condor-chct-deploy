BLOCK_NUMBER="$1"
EPOCHS="$2"
MAX_REG_COUNT="$3"

echo "MAX_REG_COUNT = $MAX_REG_COUNT, Block Number = $BLOCK_NUMBER, EPOCHS = $EPOCHS"
git clone https://github.com/madgraph5/madgraph4gpu.git
cd madgraph4gpu
export MADGRAPH4GPU_HOME=`pwd`
cd epochX/cudacpp/gg_ttgg.sa/SubProcesses/P1_Sigma_sm_gg_ttxgg
sed -i "s/###CUFLAGS+= --maxrregcount 128/CUFLAGS+= --maxrregcount $MAX_REG_COUNT/" makefile
sed -i 's/sudo//g' profile.sh
cat makefile | grep "CUFLAGS+="
make cleanall
make AVX=avx2 FPTYPE=d HELINL=0
sh profile.sh -p $BLOCK_NUMBER 256 $EPOCHS
