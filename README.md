# bug_code
记录遇到的bug，家人们来帮我解决一下!!!

1. tutorial.py
   其中是有一个print会重复运行，且没有理由。经测试，在windows11上，python3.10，torch2.0.1, torchvision0.15.2 conda环境中出现了这个问题，目前没有解决，在ubuntu服务器上测试没有这个问题
2. 有些平台，你分配16G内存会报错Killed，然后也无法通过demsg来输出错误原因。
   ![image](https://github.com/user-attachments/assets/957aa199-5b4a-40c1-b477-aa6d5ae8a2fa)
   ![image](https://github.com/user-attachments/assets/a1053901-05ab-4dcd-a6cc-2232e33d5145)
   ![image](https://github.com/user-attachments/assets/e9e5a975-7aec-4d7b-b701-1c9bbeffe7e2)

3. 相同的pytorch数据，在同一块gpu上进行相同操作，得到的结果不一样。
