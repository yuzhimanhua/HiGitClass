# HiGitClass: Keyword-Driven Hierarchical Classification of GitHub Repositories
This project focuses on hierarchical _dataless_ GitHub repository classification.

## Installation
For training, a GPU is strongly recommended. CPU is supported but training could be slow (30-40 mins in our experiments).

### Keras
The code is based on Keras. You can find installation instructions [**here**](https://keras.io/#installation).

### Dependency
The code is written in Python 3.6. The dependencies are summarized in the file ```requirements.txt```. You can install them like this:

```
pip3 install -r requirements.txt
```

## Quick Start
To reproduce the results in our paper, you need to first download the datasets and the embedding files. The **Machine-Learning** dataset (named ```ai.zip```) can be downloaded [**here**](https://drive.google.com/file/d/1vyoSzsL3KwmRKd7mDpdWaCzcUVADdYHW/view?usp=sharing). The **Bioinformatics** dataset (named ```bio.zip```) can be downloaded [**here**](https://drive.google.com/file/d/1PpikOHSWQ61lO0sDsBnijwj56lOtmVlR/view?usp=sharing). Then you need to unzip them and put them under the main folder ```./```. Then the following running script can be used to run the model.

```
./test.sh
```

Level-1/Level-2/Overall Micro-F1/Macro-F1 scores will be shown in the last several lines of the output. The classification result can be found under your dataset folder. For example, if you are using the **Bioinformatics** dataset, the output will be ```./bio/out.txt```.

## Data
Two datasets, **Machine-Learning** and **Bioinformatics**, are used in our paper. Besides the "input" version mentioned in the Quick Start section, we also provide the [**json version**](https://drive.google.com/file/d/1C7V9Ww-ZaoWqaHdNR_fryXfEmZEowYXK/view?usp=sharing), where each line is a json file with user name, text (description + README), tags, repo name, upper-level label and lower-level label. An example is shown below.

```
{  
   "id":1,
   "user":"Natsu6767",
   "text":"PyTorch Implementation of DCGAN trained on the CelebA dataset . # Deep Convolutional GAN ...",
   "tags":[  
      "pytorch",
      "dcgan",
      "gan",
      "implementation",
      "deeplearning",
      "computer-vision",
      "generative-model"
   ],
   "super_label":"$Computer-Vision",
   "sub_label":"$Image-Generation",
   "repo_name_seg":"DCGAN PyTorch",
   "repo_name":"Natsu6767/DCGAN-PyTorch"
}
```

|Dataset | #Repositories | #Classes | Leaf class name| 
| ------------- |-------------| -----| ---------- |
| Machine-Learning | 1,596 | 3+14 | Image Generation, Object Detection, Image Classification, Semantic Segmentation, Pose Estimation,  Super Resolution, Text Generation, Text Classification, Named Entity Recognition, Question Answering, Machine Translation, Language Modeling, Speech Synthesis, Speech Recognition|
| Bioinformatics | 876 | 2+10 | Sequence Analysis, Genome Analysis, Gene Expression, Systems Biology, Genetics and Population Analysis, Structural Bioinformatics, Phylogenetics, Text Mining, Bioimaging, Database and Ontologies|

## Embedding
We use [**ESim**](https://github.com/shangjingbo1226/ESim) in the embedding module. In the Quick Start section, we include a pretrained embedding file in the downloaded folders. If you would like to retrain the embedding (or **you have a new dataset**), please follow the steps below.

1. Create a directory named ```${dataset}``` under the main folder (e.g., ```./bio```).

2. Prepare three files: (1) ```./${dataset}/doc_id.txt``` containing labeled document ids for each class. Each line begins with the class id (starting from ```0```), followed by a colon, and then document ids in the corpus (starting from ```0```) of the corresponding class separated by commas; (2) ```./${dataset}/dataset.csv```; and (3) ```./${dataset}/dataset.json```. **You can refer to the example datasets ([doc_id/csv](https://drive.google.com/file/d/1rtbkQOdb6stFNvQk_Iossenr7kqYQjr4/view?usp=sharing) and [json](https://drive.google.com/file/d/16ebzkNkS4m3NBjAkpSO3XBkFpAzu-RJb/view?usp=sharing)) for the format.**

3. ```cd ESim/``` and install the dependencies [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page) and [GSL](https://www.gnu.org/software/gsl/).

4. ```./run.sh```. Make sure you have changed the dataset name. The embedding file will be saved to your dataset folder (e.g., ```../bio/embedding_esim```).

With the embedding file, you can train the classifier as mentioned in Quick Start.
Please always refer to the example datasets when adapting the code for a new dataset.
