# 😀😃🥰
Welcome to Deep Lerning Model Training Toolkit. Donot worry, even if you are a rookie I will provide you full guidance on how to setup, build your own image classification model, test the model and deploy the model as well. I won't be like most of the people who just dump their code on github and lead you to void. I assure you that you can build your own model. I will be very precise and make you aware of any errors that I faced so you will get insights on how to solve those errors on your own. I will try to be informal as possible because I believe formality cannot let our brain explore the infinite. 

## Important
- This guide will be helpful to those who want to train the model using nvidia gpu's or integrated gpu. I donot have any idea on setting up Radeon GPUs to train the model, so you need to figure out that on your own.
- Using dedicated gpu will make the training extremly fast as compared to integrated GPU so it is recommended to use a dedicated graphics card for training.
- If you just want to see how it works and you donn't mind using dedicated GPU then you can directly jump to Step 3
- I feel its better to setup the python virtual environment and necessary packages first and later on setting up dedicated GPU as it will be easy for both the users.
## Step 1: Setting Virtual Environment & Necessary Packages
### Necessary tools & packages
1. Anaconda (highly recommended) Link: https://www.anaconda.com/ . Its a piece of cake setting up anaconda in windows, but if you are a linux user you might face small problems, but putting up small extra effort you can easily do so. 
   Watch this video to setup anaconda in linux ( assuming a debian distribution) : https://youtu.be/PHkCmuzgHOo
2. Packages. You need the following packages, because we call different functions and methods from these packages in our code. The most important one is tensorflow.
- Python 3.8.0
- numpy  1.20.3
- matplotlib 3.7.0
- scikit-learn 1.3.2
- scipy 1.10.1
- tensorflow 2.10.0
### Anaconda Environment Setup with TensorFlow & other package dependencies

To set up an Anaconda environment with TensorFlow, follow these steps:

1. Create a new environment named 'tensorflow-gpu' with Python version 3.8:

    ```bash
    conda create --name tensorflow-gpu python=3.8
    ```

2. Activate the environment:

    ```bash
    conda activate tensorflow-gpu
    ```

3. Install TensorFlow version 2.10.0:

    ```bash
    pip install tensorflow==2.10.0
    ```

4. Enable notebook support in the environment:

    ```bash
    conda install -y -c conda-forge nb_conda
    ```

5. Add the environment to Jupyter Kernel:

    ```bash
    python -m ipykernel install --user --name tensorflow-gpu --display-name "Python 3.8 (tensorflow-gpu)"
    ```
6. Install the mentioned version of packages (As we already installed tensorflow and the required ython version, so we will not reinstall them. We will install other packages that I mentioned above. Please
   donot copy and paste the code below directly. I want to show you it's in the following format. 
   ```bash
   pip install mentioned_package_name==mentioned_package_version
   ```
   - So for numpy
   ```bash
   pip install numpy==1.20.3
   ```
After opening Jupyter Notebook, change the kernel from Python to Python 3.8 (tensorflow-gpu).
(Image section) 

