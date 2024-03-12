# I identify as an Individual 

## Abstract
Imagine a team of dedicated wildlife researchers struggling to identify individual elephants from countless photos. Currently, they meticulously analyze each image, noting specific features like tail markings or ear shape, by hand. This process limits their ability to study larger populations.
This is where our research comes in. We're partnering with these ecologists to automate this classification process. Instead of reinventing the wheel, we'll leverage their expertise. They've identified a crucial set of features – shape of the ear, presence of tusks, shape of the ear lobe, tail positions and a 100 others - that act like an animal's fingerprint.
Our task is to build an AI system using deep learning and computer vision techniques. This system will analyze photos automatically, recognizing those key features identified by the ecologists. Essentially, it'll learn to "see" the same way the researchers do, but at lightning speed.
By automating feature extraction, we'll free up the researchers' time for more analysis and discovery. They can finally focus on the bigger picture, studying population trends and animal behavior with a newfound efficiency. This collaboration between cutting-edge AI and ecological expertise holds the potential to revolutionize how we study the natural world.


### Current Workflow:

  1. Ecologists visually analyze images of individuals.
  2. Based on this analysis, they manually input values for over 100 parameters, such as ear shape, presence of tusks and others into a system.
  3. The system utilizes these inputs to generate a probabilistic score for individual identification.

### Automation Approach:

  1. Analyze images using various deep learning techniques.
  2. Extract relevant features automatically.
  3. Provide accurate input data to the existing scoring system.

## POC Methodology 
Any Machine learning system requires four stages in it's development process.
1. Datasets
2. Training
3. Testing
4. Depoyment

And each of these stages have further granularity in order to be completely usable by the next stages. 
1. Datasets - Data is provided by Feral in a 
