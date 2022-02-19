# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:46:43 2022

@author: Ronald Nyasha Kanyepi
@email : kanyepironald@gmail.com
"""

import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import wikipedia
import pyjokes
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


def config():
    file_path = "./components/img/"
    img = Image.open(os.path.join(file_path, 'logo.ico'))
    st.set_page_config(page_title='VIRTUAL ASSISTANT', page_icon=img, layout="wide", initial_sidebar_state="expanded")

    # code to check turn of setting and footer
    st.markdown(""" <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)

    # encoding format
    encoding = "utf-8"

    st.markdown(
        """
        <style>
            .stProgress > div > div > div > div {
                background-color: #1c4b27;
            }
        </style>""",
        unsafe_allow_html=True,
    )

    st.balloons()
    # I want it to show balloon when it finished loading all the configs


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[11].id)
    # engine.setProperty('voice', 'english+f4')
    engine.say(text)
    engine.runAndWait()


def input_from_user():
    command = ""
    try:
        with sr.Microphone() as source:
            listener = sr.Recognizer()
            voice = listener.listen(source, timeout=3, phrase_time_limit=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'zim' in command:
                command = command.replace('zim', '')
                st.write(command)
    except:
        pass
    return command


def run_virtual_assistant(choice):
    col1,col2=st.columns(2)
    with col1:
        st.write("listening.........")
    with col2:
        pass
    while choice == "Home":
        command = input_from_user()
        with col1:
            pass
        with col2:
            st.write(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song +' from youtube')
            pywhatkit.playonyt(song)
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + current_time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            st.write(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')

        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            pass

def other_tab():
    st.header("Other TAB")


def main():
    config()
    choice = option_menu(None, ["Home", "Other Tab", "Other Tab 2", 'Other Tab 3'],
                         icons=['house', 'cloud-upload', "list-task", 'gear'],
                         menu_icon="cast", default_index=0, orientation="horizontal")
    run_virtual_assistant(choice) if (choice == "Home") else other_tab()


if __name__ == '__main__':
    main()
