# from loader import bot, dp
# from aiogram.types import Message
import openai
import os
import pandas as pd
import subprocess

# age_list = ['18', '20', '30', '40', 'se', '60', '90']
#
# gender_list = ['man', 'woman']
#
# power_list =
# ['invisibility', "read in the thoughts",
# "turning lead into gold", 'immortality', 'telepathy', 'teleport', 'flight']


openai.api_key = os.getenv('RAPID_API_KEY')


def create_superhero(age, gender, power):
    prompt_words = "Imagine a complete and detailed description of a {age}-year-old {gender} fictional character who has the superpower of {power} Write out the entire description in a maximum of 100 words in great detail:"

    sub_prompt_info = "{age}, {gender}, {power}"

    df = pd.DataFrame()

    for i in range(3):
        prompt = prompt_words.format(age=age, gender=gender, power=power)
        sub_prompt = sub_prompt_info.format(age=age, gender=gender, power=power)

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        finish_reason = response["choices"][0]["finish_reason"]
        response_txt = response["choices"][0]["text"]
        new_row_dict = {
            'age': age,
            'gender': gender,
            'power': power,
            'prompt': prompt,
            'sub_prompt': sub_prompt,
            'response_txt': response_txt,
            'finish_reason': finish_reason
        }
        new_row = pd.DataFrame([new_row_dict])
        df = pd.concat([df, new_row], axis=0, ignore_index=True)
    df.to_csv("out_openai.csv")


def open_scv():
    df = pd.read_csv("out_openai.csv")
    prepared_data = df.loc[:, ['sub_prompt', 'response_txt']]
    prepared_data.rename(columns={'sub_prompt': 'prompt', 'response_txt': 'completion'}, inplace=True)
    prepared_data.to_pickle("prepared_data.csv")

    subprocess.run('openai tools fine_tunes.prepare_data -- file prepare_data.scv --quiet'.split())

    subprocess.run('openai api fine_tunes.create --training_file prepared_data_prepared.jsonl --model davinci --suffix "SuperHero"'.split())


create_superhero('18', 'man', 'immortality')
open_scv()
