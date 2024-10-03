# How we are using label studio

03-10-2024

We are using label-studio for annotation, where we are feeding our local files for annotation. Basically the images are been fed from `/opt/label-studio-data` of label-stud container. The images in the above given path are fetched by the scheduler where the model has not properly identified.
<br>
<br>
[Read this to understand why we are using scheduler]().

## Test the label-studio

- Get the credentails of label-studio from `Mr Surya`.
- Checkout `labels.cialabs.org`
- Login with credentials.
- Read this to understand how the image feeding works [here]().
- Now you are good to annotate images

> Note: Syncing has to be done manually, since there is no automation available.
