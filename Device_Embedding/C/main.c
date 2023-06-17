#include <stdio.h>
#include <opencv2/opencv.h>
#include <wiringPi.h>

#define BUZZER_PIN 32 

int main()
{
	// 카메라 구동 및 이미지 저장 
	cv::VideoCapture cap(0);
	if (!cap.isOpened()) {
		printf("Cannot open camera.\n");
		return -1;
	}
	
	cv::Mat frame; // mat 객체를 생성하여 프레임을 저장할 변수를 만듦 
	cap.read(frame); // 첫번째 프레임 읽기 

	if (frame.empty()) {
		printf("Cannot read frame.\n");
		return -1;
	}

	cv::namedWindow("Camera", cv::WINDOW_NORMAL);
	cv::imshow("Camera", frame);

	char key = cv::waitKey(1);
	while (key != 'q'){ // 'q' 입력전까지 무한루프 
		cap.read(frame); // 프레임 읽기 
		if (frame.emptry()){
			printf("Cannot read frame.\n");
			break;
		}

		cv::imshow("Camera", frame);

		if (key == 's'){
			// 현재 프레임을 이미지로 저장 
			char filename[20];
			sprintf(filename, "image%d.jpg", time(NULL));
			if (cv::imwrite(filename, frame)){
				printf("image saved: %s\n", filename);
			}else {
				printf("failed to save.\n");
			}
		}
		key = cv::waitKey(1);
	}

	cap.release(); // 카메라 닫기 
	cv::destroyAllWindows();

	// yolov5s tflite 모델 로드 및 실행 
	system("python3 detect.py --weights yolov5s-fp16.tflite --img 640 --conf 0.25 --source image1.jpg --save-txt ");

	// buzzer 작동 코드 
	// 결과 테스트 파일 읽기

	File *file;

	char filename[] = "image1.txt";
	char line[100];

	// 파일 열기 
	file = fopen(filename, "r");
	if (file == NULL){
		printf("Cannot open file.\n");
		return 1;
	}

	// 파일 내용 읽기 
	while (fgets(line, sizeof(line), file) != NULL){
		printf("%s", line);
	}

	// 파일 닫기 
	fclose(file);

	// buzzer 작동 
	if (wiringPiSetupGpio() == -1){
		printf("failed to WiringPi library initialization");
		return -1;
	}

	if (sizeof(line)>1){
		pinMode(BUZZER_PIN, OUTPUT); // 핀모드 설정 
		digitalWrite(BUZZER_PIN, HIGH); // 버저 울리기 
		delay(500); // 0.5초 대기 
		digitalWrite(BUZZER_PIN, LOW); // 버저 끄기 
		delay(500); // 0.5초 대기 
	}
	return 0;
}
