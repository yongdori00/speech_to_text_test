#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def run_quickstart():
    # [START speech_quickstart]
    import io
    import os
    import sys

    # Imports the Google Cloud client library
    # [START speech_python_migration_imports]
    from google.cloud import speech

    # [END speech_python_migration_imports]

    # Instantiates a client
    # [START speech_python_migration_client]
    client = speech.SpeechClient()
    # [END speech_python_migration_client]

    # The name of the audio file to transcribe
    output_name = input("새로 작성할 파일 이름을 적어주세요.")
    output_name += '.txt'
    file_name = os.path.join(os.path.dirname(__file__), ".", "file.wav")
    write_file_name = open(output_name, 'w')

    # Loads the audio into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        write_file_name.write(format(result.alternatives[0].transcript))
    # [END speech_quickstart]
    write_file_name.close()

if __name__ == "__main__":
    run_quickstart()