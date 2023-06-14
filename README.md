# Condor CHCT Deployment

## Nvidia NSight Compute Singularity Container Deployment

This repo holds the required defination file and steps for deploying Nvidia Nsight with CUDA support container over Condor clusters and perform relevant studies requiring GPU support. Ex - Madgraph4GPU

Follow the steps below for using the resources available in the repo:

```
// This will build a singularity image from the definition file available in the repo
// Replace the names in {} with relevant names

sudo singularity build {image_name}.sif {singularity_def_file}.def
```

Once the image is build it can be deployed in a standalone environment on any system with singularity as below:

```
singularity run {image_name}.sif
```

To perform a task/job using the image over condor system, manipulate the run_script.sh file and the job.submit file. The example of these are mentioned in the repo. Following this Submit the job to condor cluster using the command below.

```
condor_submit job.submit
condor_q // for checking status
```

