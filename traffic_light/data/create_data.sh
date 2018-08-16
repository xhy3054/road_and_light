# !/bin/bash

caffe_root_dir="/home/night/traffic_light/caffe-ssd"

#the current path should be "/home/night/traffic_light/"
current_dir=`pwd`
# we changed data root dir and data_ser_name and label_type
redo=1
# this is your root data dir
data_root_dir="$current_dir/data/LISA"
# using this access your caffe/data/dataset dir, trainval.txt and test.txt in it
dataset_name="LISA"
# your map file
mapfile="$current_dir/models/labelmap_lisa.prototxt"
echo $mapfile
anno_type="detection"
label_type="txt"
db="lmdb"
min_dim=0
max_dim=0
width=0
height=0

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ] 
then
  extra_cmd="$extra_cmd --redo"
fi
for subset in test trainval
do
  python $caffe_root_dir/scripts/create_annoset.py --anno-type=$anno_type --label-type=$label_type --label-map-file=$mapfile --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height --check-label $extra_cmd $data_root_dir $current_dir/$subset.txt $data_root_dir/$db/$dataset_name"_"$subset"_"$db examples/$dataset_name
done
