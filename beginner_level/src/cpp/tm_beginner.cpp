#include "opencv2/imgcodecs.hpp" //for image reading and writing
#include "opencv2/highgui.hpp"	//for graphical user interface
#include "opencv2/imgproc.hpp"	//for image processing
#include <iostream>	//standard io library

int main()
{
	//reading the test and template images in BGR format
	cv::Mat img_rgb = cv::imread("../../images/test_image.png", cv::IMREAD_COLOR); 
	cv::Mat template_rgb = cv::imread("../../images/template_image.png", cv::IMREAD_COLOR);

	if (img_rgb.empty() || template_rgb.empty())
	{	//if either of those images is empty, exit from the main function with -1
		std::cout << "Error reading file(s)!" << std::endl;
		return -1;
	}

	//converting the images into grayscale
	cv::Mat img_gray, template_gray;	
	cv::cvtColor(img_rgb, img_gray, cv::COLOR_BGR2GRAY);
	cv::cvtColor(template_rgb, template_gray, cv::COLOR_BGR2GRAY);

	//canny edge detection for the grayscale images
	const int low_canny = 110;
	cv::Canny(img_gray, img_gray, low_canny, low_canny * 3);
	cv::Canny(template_gray, template_gray, low_canny, low_canny * 3);

	//displaying the converted grayscale images
	cv::imshow("Test image", img_gray);
	cv::imshow("Template image", template_gray);

	//template matching using cross coefficient normalized method
	cv::Mat res_32f(img_rgb.rows - template_rgb.rows + 1, img_rgb.cols - template_rgb.cols + 1, CV_32FC1);
	matchTemplate(img_gray, template_gray, res_32f, cv::TM_CCOEFF_NORMED);

	//converting into a single byte single channel image for adaptive thresholding and displaying
	cv::Mat res;
	res_32f.convertTo(res, CV_8U, 255.0);
	cv::imshow("Result", res);

	//adaptive thresholding to binarise the image to get the max value and max location
	int size = ((template_rgb.cols + template_rgb.rows) / 4) * 2 + 1; 
	adaptiveThreshold(res, res, 255, cv::ADAPTIVE_THRESH_MEAN_C, cv::THRESH_BINARY, size, -64);
	cv::imshow("Result_threshold", res);

	while (1)
	{
		//finding the max value and max location
		double minval, maxval;
		cv::Point minloc, maxloc;
		minMaxLoc(res, &minval, &maxval, &minloc, &maxloc);

		if (maxval > 0)
		{
			//draw rectangles with the dimensions of the template image in the test image 
			cv::rectangle(img_rgb, maxloc, cv::Point(maxloc.x + template_rgb.cols, maxloc.y + template_rgb.rows), cv::Scalar(0, 0, 0), 2);
			cv::floodFill(res, maxloc, 0);
		}
		else
			break;
	}
	//eventually, display and save the resultant image 
	cv::imshow("Final Result", img_rgb);
	cv::imwrite("../../images/Final.png", img_rgb);
	cv::waitKey(0);

	return 0;
}
