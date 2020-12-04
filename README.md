# DI-Sport-Analysis
This is the data challenge project - Sport Analysis in UoE Design Informatics.

## About the Data
The data contains footballers' personal information, their membership of different teams, and their performance in different competitions and seasons.

## Project Objective
We aim to explore factors of team success in professional football domain, in terms of combinations of players including their career paths, diversity of ages, nationalities and so on.

## Structure Description
- Data_Process - Source codes to process the data.
- Data_Selected - Data selected for the visualization.

## Data visualization
Based on our theoretical and data research, we made a visual design for team diversity and cohesion.
Generally, we combined the index of players, their nationalities, career path, and age into this chart. We divide a circle into 16 sectors, representing 16 main players and we group players by their nationalities and the past careers to better show cohesion. You could see there are 10 layers representing the past 10 seasons, and we use different colors for different teams. This show the teams that a player joined in the past 10years.The outermost circle represents nationality, and the color is based on the national flag color. In terms of ages, we visualize them through the line. This is also an age baseline circle.A player is relatively old if his age line crosses the baseline.We may also see the overall team age through these lines.
We also design these pictures to find players who have played together.

## How to Run Programs in Data_Process?
Since Github limits the size of every single file uploaded to be smaller than 100MB, I was not able to upload our datasets here. Therefore, currently if you want to run programs in Data_Process, you need to put our datasets into a folder named 'sport_datasets', and put the folder into the same dictionary of this project (your local dictionary). Then the data can be loaded successfully.

If you are adding new programs that process the datasets, please also set file paths as '../../sport_datasets/FileName'.
