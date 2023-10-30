#!/bin/bash

mp4_path=$1
h264_path=$2

for file in $(ls $mp4_path)
do
  #echo "${file}"
  echo "${h264_path}/${file%.*}.mp4"
  ffmpeg -i "${mp4_path}/${file%.*}.mp4" -codec copy -bsf: h264_mp4toannexb -f h264 "${h264_path}/${file%.*}.h264"
  mv "${h264_path}/${file%.*}.h264" "${h264_path}/${file%.*}.264"
done