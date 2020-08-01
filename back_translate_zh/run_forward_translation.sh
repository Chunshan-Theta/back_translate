
replicas=1
worker_id=0
sampling_temp=0.8


# Dirs
data_dir=back_trans_data
doc_len_dir=${data_dir}/doc_len
forward_src_dir=${data_dir}/forward_src
forward_gen_dir=${data_dir}/forward_gen
backward_gen_dir=${data_dir}/backward_gen
para_dir=${data_dir}/paraphrase



echo "*** forward translation ***"
t2t-decoder \
  --problem=translate_enfr_wmt32k \
  --model=transformer \
  --hparams_set=transformer_big \
  --hparams="sampling_method=random,sampling_temp=${sampling_temp}" \
  --decode_hparams="beam_size=1,batch_size=16" \
  --checkpoint_path=checkpoints/enfr/model.ckpt-500000 \
  --output_dir=/tmp/t2t \
  --decode_from_file=${forward_src_dir}/file_${worker_id}_of_${replicas}.txt \
  --decode_to_file=${forward_gen_dir}/file_${worker_id}_of_${replicas}.txt \
  --data_dir=checkpoints
