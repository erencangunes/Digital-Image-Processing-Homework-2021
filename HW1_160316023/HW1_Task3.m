 RGB = imread('picasso.png');

 gray= rgb2gray(RGB);

 binary = im2bw(gray);

 subplot(2,2,1);imshow(RGB); title('RGB');
 subplot(2,2,2);imshow(gray); title('Grayscale');
 subplot(2,2,3);imshow(binary); title('Binary');
 subplot(2,2,4);imhist(RGB); title('Histogram');