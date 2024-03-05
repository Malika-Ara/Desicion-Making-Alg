# Desicion-Making-Alg

**Overview**
This repository contains a Python script for a decision-making algorithm that ranks projects according to specified criteria. The algorithm evaluates projects' alignment with specific goals and uses a scoring system to determine their relevance. The primary goal is to help with project prioritization and decision-making processes.

**Features**
_Interactive Input:_ The script allows users to enter project details such as the project name, specificity score, relevance score, and effectiveness score.
_Scoring System_: Projects are evaluated based on goal specificity, target population relevance, and the efficacy of project methods. The scoring system is adjustable, allowing for changes in the weights assigned to each criterion.
_Ranking_: The algorithm ranks projects according to their total scores, taking into account the specified acceptance cutoff

**Usage**
Run the script by calling the main() function.
Enter the number of projects when prompted.
Enter project information, including specificity, relevance, and effectiveness scores.
The script will display a ranked list of projects that meet the specified cutoff.

**Customization**
_Weights_: Using the weights dictionary, adjust the weights for specificity, relevance, and effectiveness.
_Cutoff:_ Change the cutoff value to specify the minimum score for project acceptance.

**Dependencies**
Python 3.x
