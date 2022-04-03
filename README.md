# HiGitClass: Keyword-Driven Hierarchical Classification of GitHub Repositories

This repository contains the source code for [**HiGitClass: Keyword-Driven Hierarchical Classification of GitHub Repositories**](https://arxiv.org/abs/1910.07115).

## Links

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Data](#data)
- [Running on New Datasets](#running-on-new-datasets)
- [Citation](#citation)


## Installation
For training, a GPU is strongly recommended.

### Keras
The code is based on Keras. You can find installation instructions [**here**](https://keras.io/#installation).

### Dependency
The code is written in Python 3.6. The dependencies are summarized in the file ```requirements.txt```. You can install them like this:

```
pip3 install -r requirements.txt
```

## Quick Start
To reproduce the results in our paper, you need to first download the datasets and the embedding files. The **Machine-Learning** dataset (```ai/```) and the **Bioinformatics** dataset (```bio/```) can be downloaded [**here**](https://drive.google.com/file/d/1jiMEej5z7zqv5cq3SKxNDFBm3NXgvKjo/view?usp=sharing). Then you need to unzip it and put the two folders under the main folder ```./```. Then the following running script can be used to run the model.

```
./test.sh
```

Level-1/Level-2/Overall Micro-F1/Macro-F1 scores will be shown in the last several lines of the output. The classification result can be found under your dataset folder. For example, if you are using the **Bioinformatics** dataset, the output will be ```./bio/out.txt```.

## Data
Two datasets, **Machine-Learning** and **Bioinformatics**, are used in our paper. Besides the "input" version mentioned in the Quick Start section, we also provide the [**json version**](https://drive.google.com/file/d/11zIqAg062IneYNdqfTMBV00n7weyvKbR/view?usp=sharing), where each line is a json file with user, text (description + README), tags, repository name, and labels. An example is shown below.

```
{
  "repo": "Natsu6767/DCGAN-PyTorch",
  "user": "Natsu6767",
  "text": "pytorch implementation of dcgan trained on the celeba dataset deep convolutional gan ...",
  "tags": [
    "pytorch",
    "dcgan",
    "gan",
    "implementation",
    "deeplearning",
    "computer-vision",
    "generative-model"
  ],
  "name": [
    "DCGAN",
    "PyTorch"
  ],
  "labels": [
    "$Computer-Vision",
    "$Image-Generation"
  ]
}
```

**NOTE: If you would like to run our code on your own dataset, when you prepare this json file, make sure you list the labels in the top-down order. For example, if the label path of your repository is ROOT-A-B-C, then the "labels" field should be \["A", "B", "C"\].**

Dataset statistics are as follows.

| Dataset | #Repositories | #Classes | Leaf class name | 
| ------- | ------------- | -------- | --------------- |
| Machine-Learning | 1,596 | 3+14 | Image Generation, Object Detection, Image Classification, Semantic Segmentation, Pose Estimation,  Super Resolution, Text Generation, Text Classification, Named Entity Recognition, Question Answering, Machine Translation, Language Modeling, Speech Synthesis, Speech Recognition |
| Bioinformatics | 876 | 2+10 | Sequence Analysis, Genome Analysis, Gene Expression, Systems Biology, Genetics and Population Analysis, Structural Bioinformatics, Phylogenetics, Text Mining, Bioimaging, Database and Ontologies |

## Running on New Datasets
We use [**ESim**](https://github.com/shangjingbo1226/ESim) in the embedding module. In the Quick Start section, we include a pretrained embedding file in the downloaded folders. If you would like to retrain the embedding (or **you have a new dataset**), please follow the steps below.

1. Create a directory named ```${dataset}``` under the main folder (e.g., ```./bio```).

2. Prepare three files:             
(1) ```./${dataset}/label_hier.txt``` indicating the parent children relationships between classes. The first class of each line is the parent class, followed by all its children classes. **The root class must be named as ROOT.** Tab is used as the delimiter.           
(2) ```./${dataset}/keywords.txt``` containing class-related keywords for each leaf class. Each line has a class name and a keyword.           
(3) ```./${dataset}/${json-name}.json```. **You can refer to the provided [json files](https://drive.google.com/file/d/11zIqAg062IneYNdqfTMBV00n7weyvKbR/view?usp=sharing) for the format. All fields except "repo" are required.**

3. Install the dependencies [**GSL**](https://www.gnu.org/software/gsl/) and [**Eigen**](http://eigen.tuxfamily.org/index.php?title=Main_Page). For Eigen, we already provide a zip file ```ESim/eigen-3.3.3.zip```. You can directly unzip it in ```ESim/```. For GSL, you can download it [here](https://drive.google.com/file/d/1UvmgrZbycC7wYAHahYGRB5pRtu6Aurhv/view?usp=sharing).

4. ```./prep_emb.sh```. Make sure you change the dataset/json names.

After that, you can train the classifier as mentioned in Quick Start (i.e., ```./test.sh```).
Please always refer to the example datasets when adapting the code for a new dataset.

## Citation
If you find the implementation useful, please cite the following paper:
```
@inproceedings{zhang2019higitclass,
  title={HiGitClass: Keyword-Driven Hierarchical Classification of GitHub Repositories},
  author={Zhang, Yu and Xu, Frank F. and Li, Sha and Meng, Yu and Wang, Xuan and Li, Qi and Han, Jiawei},
  booktitle={ICDM'19},
  pages={876--885},
  year={2019},
  organization={IEEE}
}
```
