#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
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

"""This application demonstrates how to perform basic operations with the
Google Cloud Vision API.
Example Usage:
python detect.py local ./resources/wakeupcat.jpg
python detect.py uri http://wheresgus.com/dog.JPG
python detect.py uri gs://your-bucket/file.jpg

"""

import argparse
import io

from google.cloud import vision


def detect_faces(path):
    """Detects faces in an image."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    faces = image.detect_faces()
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(face.emotions.anger))
        print('joy: {}'.format(face.emotions.joy))
        print('surprise: {}'.format(face.emotions.surprise))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in face.bounds.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
        print ('\n\n')


def detect_faces_uri(uri):
    """Detects faces in the file located in Google Cloud Storage or the web."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    faces = image.detect_faces()
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(face.emotions.anger))
        print('joy: {}'.format(face.emotions.joy))
        print('surprise: {}'.format(face.emotions.surprise))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in face.bounds.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
        print ('\n\n')

def detect_labels(path):
    """Detects labels in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    labels = image.detect_labels()
    print('Labels:')

    for label in labels:
        print(label.description)
    print ('\n\n')

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    labels = image.detect_labels()
    print('Labels:')

    for label in labels:
        print(label.description)
    print ('\n\n')


def detect_landmarks(path):
    """Detects landmarks in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    landmarks = image.detect_landmarks()
    print('Landmarks:')

    for landmark in landmarks:
        print(landmark.description)
    print ('\n\n')


def detect_landmarks_uri(uri):
    """Detects landmarks in the file located in Google Cloud Storage or on the
    Web."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    landmarks = image.detect_landmarks()
    print('Landmarks:')

    for landmark in landmarks:
        print(landmark.description)
    print ('\n\n')


def detect_logos(path):
    """Detects logos in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    logos = image.detect_logos()
    print('Logos:')

    for logo in logos:
        print(logo.description)
    print ('\n\n')


def detect_logos_uri(uri):
    """Detects logos in the file located in Google Cloud Storage or on the Web.
    """
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    logos = image.detect_logos()
    print('Logos:')

    for logo in logos:
        print(logo.description)
    print ('\n\n')


def detect_safe_search(path):
    """Detects unsafe features in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    safe = image.detect_safe_search()
    print('Safe search:')
    print('adult: {}'.format(safe.adult))
    print('medical: {}'.format(safe.medical))
    print('spoofed: {}'.format(safe.spoof))
    print('violence: {}'.format(safe.violence))
    print ('\n\n')


def detect_safe_search_uri(uri):
    """Detects unsafe features in the file located in Google Cloud Storage or
    on the Web."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    safe = image.detect_safe_search()
    print('adult: {}'.format(safe.adult))
    print('medical: {}'.format(safe.medical))
    print('spoofed: {}'.format(safe.spoof))
    print('violence: {}'.format(safe.violence))
    print ('\n\n')


def detect_text(path):
    """Detects text in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    texts = image.detect_text()
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in text.bounds.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    print ('\n\n')


def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    texts = image.detect_text()
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in text.bounds.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    print ('\n\n')


def detect_properties(path):
    """Detects image properties in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    props = image.detect_properties()
    print('Properties:')

    for color in props.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))
    print ('\n\n')


def detect_properties_uri(uri):
    """Detects image properties in the file located in Google Cloud Storage or
    on the Web."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    props = image.detect_properties()
    print('Properties:')

    for color in props.colors:
        print('frac: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))
    print ('\n\n')


def detect_web(path):
    """Detects web annotations given an image."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    notes = image.detect_web()

    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved')

        for page in notes.pages_with_matching_images:
            print('Score : {}'.format(page.score))
            print('Url   : {}'.format(page.url))

    if notes.full_matching_images:
        print ('\n{} Full Matches found: '.format(
               len(notes.full_matching_images)))

        for image in notes.full_matching_images:
            print('Score:  {}'.format(image.score))
            print('Url  : {}'.format(image.url))

    if notes.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(
               len(notes.partial_matching_images)))

        for image in notes.partial_matching_images:
            print('Score: {}'.format(image.score))
            print('Url  : {}'.format(image.url))

    if notes.web_entities:
        print ('\n{} Web entities found: '.format(len(notes.web_entities)))

        for entity in notes.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))
        print ('\n\n')


def detect_web_uri(uri):
    """Detects web annotations in the file located in Google Cloud Storage."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    notes = image.detect_web()

    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved')

        for page in notes.pages_with_matching_images:
            print('Score : {}'.format(page.score))
            print('Url   : {}'.format(page.url))

    if notes.full_matching_images:
        print ('\n{} Full Matches found: '.format(
               len(notes.full_matching_images)))

        for image in notes.full_matching_images:
            print('Score:  {}'.format(image.score))
            print('Url  : {}'.format(image.url))

    if notes.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(
               len(notes.partial_matching_images)))

        for image in notes.partial_matching_images:
            print('Score: {}'.format(image.score))
            print('Url  : {}'.format(image.url))

    if notes.web_entities:
        print ('\n{} Web entities found: '.format(len(notes.web_entities)))

        for entity in notes.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))
        print ('\n\n')

def detect_crop_hints(path):
    """Detects crop hints in an image."""
    vision_client = vision.Client()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision_client.image(content=content)

    hints = image.detect_crop_hints({1.77})

    for n, hint in enumerate(hints):
        print('\nCrop Hint: {}'.format(n))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in hint.bounds.vertices])

        print('bounds: {}'.format(','.join(vertices)))
        print ('\n\n')


def detect_crop_hints_uri(uri):
    """Detects crop hints in the file located in Google Cloud Storage."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    hints = image.detect_crop_hints({1.77})
    for n, hint in enumerate(hints):
        print('\nCrop Hint: {}'.format(n))

        vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in hint.bounds.vertices])

        print('bounds: {}'.format(','.join(vertices)))
        print ('\n\n')


def detect_document(path):
    """Detects document features in an image."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    document = image.detect_full_text()

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            print('Block Content: {}'.format(block_text))
            print('Block Bounds:\n {}'.format(block.bounding_box))
    print ('\n\n')


def detect_document_uri(uri):
    """Detects document features in the file located in Google Cloud
    Storage."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    document = image.detect_full_text()

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            print('Block Content: {}'.format(block_text))
            print('Block Bounds:\n {}'.format(block.bounding_box))
    print ('\n\n')


def run_local(args):
    detect_faces(args.path)
    detect_labels(args.path)
    detect_landmarks(args.path)
    detect_text(args.path)
    detect_logos(args.path)
    detect_safe_search(args.path)
    detect_properties(args.path)
    detect_web(args.path)
    detect_crop_hints(args.path)
    detect_document(args.path)


def run_uri(args):
    detect_text_uri(args.uri)
    detect_faces_uri(args.uri)
    detect_labels_uri(args.uri)
    detect_landmarks_uri(args.uri)
    detect_logos_uri(args.uri)
    detect_safe_search_uri(args.uri)
    detect_properties_uri(args.uri)
    detect_web_uri(args.uri)
    detect_crop_hints_uri(args.uri)
    detect_document_uri(args.uri)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    local_parser = subparsers.add_parser(
        'local')
    local_parser.add_argument('path')

    uri_parser = subparsers.add_parser(
        'uri')
    uri_parser.add_argument('uri')

    args = parser.parse_args()
    print args

    if ('uri' in args.command):
        run_uri(args)
    else:
        run_local(args)
