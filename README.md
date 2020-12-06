# DI-Sport-Analysis
This is the data challenge project - Sport Analysis in UoE Design Informatics.

## Dataset Description
The data describes 44,259 football players and the teams they represented from 2000/2001 to 2018/2019 in three files: person.csv, membership.csv and stat.csv. Each record contains a unique player id, allowing efficient indexing of player information between datasets.

## Theoretical Context
Structural fold: the overlap of groups that have differing previous experience within a team. For example, if two football teams merge to create one, there may be some players who have represented both teams, creating an overlap in experience – these players would represent the structural fold. The 'Game Changer' paper argues that to generate creative success, there should be a variety of past experiences within a team, otherwise a reduction of innovation will lead to conformity. However, this variety of experience stresses the importance of the structural fold – to channel communication and create common understanding, attributing to success.

## Project Objective
We aim to study how structural folding in teams influences team performance. To study this structural folding, two main factors are considered: team diversity and team cohesion. Teams with greater variety of ages, past careers (clubs) or national team experiences will be considered more diverse, while higher cohesion is defined by greater shared past experience in a team, including the seasons played in the current team. Team cohesion is therefore a measure of the overlap of current team members’ previous memberships. Position in the league is used as a measure of team performance.

## Structure Description
- Backgroud_Theory - Literature research about culture overlap.
- Data_Process - Source codes to for data processing and analysis.
- Data_Selected - Data selected for the visualization.
- Data_Visualization - Data visualization prototype.

## Data visualization
Based on our objective, we made a visual design to present player combinations intuitively.
A particular team during a particular season is represented in a sunburst-like chart made up of players’ previous experience. The chart shows the 16 main players with their ages, nationalities, and career paths in past 10 seasons. The charts are integrated in an interface and with interactive operations for users to see some details of team diversity and cohesion (see our demonstration video for the prototype).

## How to Run Programs in Data_Process?
Since Github limits the size of every single file uploaded to be smaller than 100MB, I was not able to upload our datasets here. Therefore, currently if you want to run programs in Data_Process, you need to put our datasets into a folder named 'sport_datasets', and put the folder into the same dictionary of this project (your local dictionary). Then the data can be loaded successfully.

If you are adding new programs that process the datasets, please also set file paths as '../../sport_datasets/FileName'.
