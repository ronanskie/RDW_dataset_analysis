# Where do the Dutch get their cars? - A data analysis

[![GitHub license](https://img.shields.io/github/license/ronanskie/RDW_dataset_analysis)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ronanskie/RDW_dataset_analysis)](https://github.com/ronanskie/RDW_dataset_analysis/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/ronanskie/RDW_dataset_analysis)](https://github.com/ronanskie/RDW_dataset_analysis/issues)

---

## 📑 Overview

The Dutch vehicle authority (RDW) keeps track of all the vehicles that are registered in the Netherlands. The dataset that results from this contains a lot of information about the vehicles and is openly available to the public. In this blog post, I analyse the data from this dataset to find out where cars in the Netherlands originate from.

In recent times, there has been a lot of discussion about Chinese car brands entering the European market at very low prices compared to their European counterparts. This made me wonder to what extent these Chinese car manufacturers have already penetrated the Dutch market and how this compares to manufacturers from other countries. Therefore, I decided to use the RDW vehicle registration dataset to create an overview of the countries of origin of cars in the Netherlands.

I wrote a blog post on my website about the analysis that I did on this dataset, you can read it by clicking the link below.

```bash
https://www.ronansmedeman.nl/blog_rdw_analysis
```

---

## 📁 Project structure

This section explains which directories you can find in the template and how you should use them.

### Directories

* **RDW_dataset_analysis:** The main project folder, contains two directories and general files like the README.md and the Python scripts. 
* **dataset:** Contains a Shell script that prepares the dataset for analysis. Also contains a CSV file with the country of origin of car manufacturers. The RDW dataset should also be placed here, not included in the repository by default.
* **output:** This is where the Python scripts place the output (i.e. the interactive world map made with the Folium library). 

---

## 🔧 How to get started

If you want to run this code yourself, you can follow the instructions below.

### Prerequisites

This code was built on **Python 3.13.3**. It is recommended to also use this version while running it yourself, but it is likely to work with different versions. 
You will also need to have **pip** installed to install the libraries from the "requirements.txt" file. The following instructions also assume you are using an **Ubuntu** based operating system, however, this is not a requirement for the code to work. If you are using Windows or MacOS you might need to use a different command in some steps. If something is not working you can google for the correct alternative command on your operating system.

### How to run

1.  **Clone the repository:**

    Open a terminal and move into the directory in which you want to place the project. Then use the below command to clone the repository. 

    ```bash
    git clone git@github.com:ronanskie/RDW_dataset_analysis.git
    cd RDW_dataset_analysis
    ```

2.  **Install dependencies:**

    To install all dependencies you first need to create a virtual environment (venv). Once one has been created, the venv needs to be activated in order to install all dependencies for the template. The " requirements.txt" file contains all the needed dependencies. Everytime that you are working on the project you will need to activate this venv using the "source venv/bin/activate" command. If you do not do this, the Python scripts will not be able to use the libraries that they need.

    ```bash
    python3 -m venv .venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Add the dataset:**

    You can download the used dataset from the url below. The downloaded CSV file should be added in the dataset directory. Note that you have to change the name of the downloaded file to "RDW_dataset.csv" for the program to work.

    ```bash
    https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen/m9d7-ebf2/about_data
    ```

4.  **Generate results:**

    When in the project directory you can use the following commands to run the program and generate the results.

    ```bash
    cd dataset
    sudo chmod +x sampler.sh #only required the first time you run the program
    ./sampler.sh
    cd ../
    python3 main.py
    ```

    The program might take a while to calculate the results depending on the speed of your computer (a few minutes is very likely). 
    Once it has finished you will find the results in the output directory. An .html file should have appeared here which you can open in your browser.
    When opening this file you should see an interactive world map with the data displayed.

---

## ⚙️ Customization

This program can be slightly customized to your liking. The sampler.sh now filters out brands with more than a 100 vehicles registered in the Netherlands.
You can reduce or increase this limit to your liking. Note however that the car_manufacturers mapping, as found in the dataset directory, might no longer map all brands when this value is lowered. In "main.py" and "output_generator.py" you can find some constant variables that you can change to your liking, mostly to change the default paths.

---

