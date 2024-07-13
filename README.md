# Decorrelation Stretch (Dstretch)

Decorrelation Stretch is an image processing technique designed for the enhancement of color differences in images. Though originally developed for remote sensing applications, decorrelation stretch has found major importance in fields such as archaeology and geology for the highlighting of faint features that are otherwise difficult to be discerned. For example, in rock paintings, DStretch can show faint paint needed in the reconstruction of rock painting panels.

The principle of dstretch works on enhancing the contrast between different colors in an image so that very subtle differences can be distinguished. It does this by transforming the color space of an image such that its color channels—usually RGB—are not correlated with one another, stretching their colors, and then transforming them back to the original space. The image is first converted to an appropriate color space, the covariance matrix of the color channels is computed, an eigenvalue decomposition of this matrix is done, and the image data is transformed to a new color space defined by the eigenvectors. The stretching of color values is performed in order to make different differences more apparent; then, data transformation back to the original color space is implemented.

## Results Examples
<p align="center">
  <img src="https://github.com/user-attachments/assets/6f8b29be-9db4-48d8-8f6e-b989282a8c4d" width="60%">
  <br><br>
  <a>  Image of rock painting in Hossa, Finland. [Taken by Veikko Miettinen and Dmitry Semenov]</a>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/436845f1-6d1e-4121-9870-c271ff1be34a" width="60%">
  <br><br>
  <a>  Image of rock painting in Atsuvansalmi, Finland. [Taken by Veikko Miettinen and Dmitry Semenov]</a>
</p>

Feel free to explore my <a href="https://github.com/YasminaDjelil?tab=repositories">other repositories</a> if you are interested in rock art in general or the study of rock art with remote sensing specifically.

