# Identity Crisis

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

## POC  
Any Machine learning system requires four stages in it's development process.
1. Datasets
2. Training
3. Testing
4. Depoyment

And each of these stages have further granularity in order to be completely usable by the next stages. 
1. **Datasets**
   - **Data Collection**   : Data is provided by Feral, where currently we have images for 5 individuals and approimately 50 each. 
   - **Data Augmentation** : The whole purpose of this process is to increase data set size, since 50 no where near enough and will                                      definetly over fit our model. We are currently not sure what kind of strategies we can use to augment data
                             because in the process of augmenting these images, we might loose ciritical information like shapes of certain                              parts of the image. For now at maximum we can do is to mirror the images. Which 2xs the data set size.
   - **Labeling Annotation** :Studies show that applying segmentation masks over the images gives us fruitful results to see shapes and                                   patterns in the image. We have worked with few tools and we decidel Label Studio is the one we will go ahead
                            with. In order to avoid then manual process of drawing polygons over features that we want the computer to see,                             we'll have to figure out a way to use SAM(Segment Anything model) and label on top of it. (In Progress)
2. **Training**
     - **Model Architecture** : We can either choose to go with a exisiting models like yolo etc or we can build our own model architecture.
                                This decision will be based on how our data looks and the areas of focus 
