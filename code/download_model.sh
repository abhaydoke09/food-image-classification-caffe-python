model_type=$1
current_dir=`pwd`
parent_dir=`dirname $current_dir`
wget -P $parent_dir/caffe_models/bvlc_$model_type http://dl.caffe.berkeleyvision.org/bvlc_$model_type.caffemodel

