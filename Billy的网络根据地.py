import streamlit as st
from PIL import Image
import time
page = st.sidebar.radio("我的首页", ["我的兴趣推荐", "我的图片处理工具", "我的智慧词典"])

def page_1():
    # 我的兴趣推荐
    with open("记念.ogg", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format="audio/mp3", start_time=0)
    st.image("背景图片.jpg")
    st.write("荷花清芳的电视剧推荐")
    st.write("《香蜜沉沉烬如霜》，《三生三世十里桃花》，《祈今朝》，《长相思》")
    st.write("------------------------------")
    st.write("荷花清芳的游戏推荐")
    st.write("《蛋仔派对》，《逆水寒》")
    st.image("蛋仔派对.png")
    st.write("------------------------------")
    st.write("荷花清芳的书籍推荐")
    st.write("《笑猫日记》，《三国演义》，《朝花夕拾》")
    st.image("川流不息专辑图片.png")
    st.write("------------------------------")
    st.write("荷花清芳的音乐推荐")
    st.write("《谪仙》，《踏山河》，《川流不息》")
    st.image("谪仙.png")
    st.write("------------------------------")
def page_2():
    # 我的图片处理工具
    st.write(":sparkles:图片换色小程序:sparkles:")
    uploaded_file = st.file_uploader("上传图片", type=["png", "jpeg", "jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(image_change(img, 0, 2, 1))
        with tab3:
            st.image(image_change(img, 1, 2, 0))
        with tab4:
            st.image(image_change(img, 1, 0, 2))

def page_3():
    # 我的智慧词典
    st.write(":sparkles:智慧词典:sparkles:")
    with open("词典.txt", "r", encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open("单词查询次数.txt", "r", encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])        
    word = st.text_input("请输入要查询的单词:")
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("单词查询次数.txt", "w", encoding="utf-8") as f:
            message = ""
            for k, v in times_dict.items():
                message += str(k) + "#" + str(v) + "\n"
            message = message[:-1]
            f.write(message)
        st.write("查询次数", times_dict[n])
        st.write("这是第", words_dict[word][0], "个单词")
        if word == "birthday" or word == "balloon":
            st.code("恭喜你触发彩蛋！这是一句祝福语：Happy Birthday!")
            st.balloons()
            st.balloons()
        if word == "snow" or word == "winter":
            st.snow()
            st.snow()
        if word == "Billy":
            st.code("啊哈！你怎么知道我的名字的？")
            st.balloons()
            st.snow()
# 初始化进度条为0
progress = st.sidebar.progress(0)
# 模拟耗时操作（这里只是一个循环）
for i in range(100):
    # 更新进度条
    progress.progress(i + 1)
    time.sleep(0.1)  # 短暂休眠模拟实际运算时间
# 当所有任务完成后，设置进度为100
progress.progress(100)

def image_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
    
if page == "我的兴趣推荐":
    page_1()
elif page == "我的图片处理工具":
    page_2()
elif page == "我的智慧词典":
    page_3()
