from typing import Any, Dict, Optional

WORDING : Dict[str, Any] =\
{
	'conda_not_activated': 'Conda is not activated',
	'python_not_supported': 'Python version is not supported, upgrade to {version} or higher',
	'ffmpeg_not_installed': 'FFMpeg is not installed',
	'creating_temp': 'Creating temporary resources',
	'extracting_frames': 'Extracting frames with a resolution of {resolution} and {fps} frames per second',
	'extracting_frames_succeed': 'Extracting frames succeed',
	'extracting_frames_failed': 'Extracting frames failed',
	'analysing': 'Analysing',
	'processing': 'Processing',
	'downloading': 'Downloading',
	'temp_frames_not_found': 'Temporary frames not found',
	'copying_image': 'Copying image with a resolution of {resolution}',
	'copying_image_succeed': 'Copying image succeed',
	'copying_image_failed': 'Copying image failed',
	'finalizing_image': 'Finalizing image with a resolution of {resolution}',
	'finalizing_image_succeed': 'Finalizing image succeed',
	'finalizing_image_skipped': 'Finalizing image skipped',
	'merging_video': 'Merging video with a resolution of {resolution} and {fps} frames per second',
	'merging_video_succeed': 'Merging video succeed',
	'merging_video_failed': 'Merging video failed',
	'skipping_audio': 'Skipping audio',
	'restoring_audio_succeed': 'Restoring audio succeed',
	'restoring_audio_skipped': 'Restoring audio skipped',
	'clearing_temp': 'Clearing temporary resources',
	'processing_stopped': 'Processing stopped',
	'processing_image_succeed': 'Processing to image succeed in {seconds} seconds',
	'processing_image_failed': 'Processing to image failed',
	'processing_video_succeed': 'Processing to video succeed in {seconds} seconds',
	'processing_video_failed': 'Processing to video failed',
	'model_download_not_done': 'Download of the model is not done',
	'model_file_not_present': 'File of the model is not present',
	'choose_image_source': 'Choose a image for the source',
	'choose_audio_source': 'Choose a audio for the source',
	'choose_video_target': 'Choose a video for the target',
	'choose_image_or_video_target': 'Choose a image or video for the target',
	'specify_image_or_video_output': 'Specify the output image or video within a directory',
	'match_target_and_output_extension': 'Match the target and output extension',
	'no_source_face_detected': 'No source face detected',
	'frame_processor_not_loaded': 'Frame processor {frame_processor} could not be loaded',
	'frame_processor_not_implemented': 'Frame processor {frame_processor} not implemented correctly',
	'ui_layout_not_loaded': 'UI layout {ui_layout} could not be loaded',
	'ui_layout_not_implemented': 'UI layout {ui_layout} not implemented correctly',
	'stream_not_loaded': 'Stream {stream_mode} could not be loaded',
	'job_created': 'Job {job_id} created',
	'job_not_created': 'Job {job_id} not created',
	'job_submitted': 'Job {job_id} submitted',
	'job_not_submitted': 'Job {job_id} not submitted',
	'job_all_submitted': 'Jobs submitted',
	'job_all_not_submitted': 'Jobs not submitted',
	'job_deleted': 'Job {job_id} deleted',
	'job_not_deleted': 'Job {job_id} not deleted',
	'job_all_deleted': 'Jobs deleted',
	'job_all_not_deleted': 'Jobs not deleted',
	'job_step_added': 'Step added to job {job_id}',
	'job_step_not_added': 'Step not added to job {job_id}',
	'job_remix_step_added': 'Step {step_index} remixed from job {job_id}',
	'job_remix_step_not_added': 'Step {step_index} not remixed from job {job_id}',
	'job_step_inserted': 'Step {step_index} inserted to job {job_id}',
	'job_step_not_inserted': 'Step {step_index} not inserted to job {job_id}',
	'job_step_removed': 'Step {step_index} removed from job {job_id}',
	'job_step_not_removed': 'Step {step_index} not removed from job {job_id}',
	'running_job': 'Running queued job {job_id}',
	'running_jobs': 'Running all queued jobs',
	'retrying_job': 'Retrying failed job {job_id}',
	'retrying_jobs': 'Retrying all failed jobs',
	'processing_job_succeed': 'Processing of job {job_id} succeed',
	'processing_jobs_succeed': 'Processing of all job succeed',
	'processing_job_failed': 'Processing of job {job_id} failed',
	'processing_jobs_failed': 'Processing of all jobs failed',
	'processing_step': 'Processing step {step_current} of {step_total}',
	'time_ago_now': 'just now',
	'time_ago_minutes': '{minutes} minutes ago',
	'time_ago_hours': '{hours} hours and {minutes} minutes ago',
	'time_ago_days': '{days} days, {hours} hours and {minutes} minutes ago',
	'point': '.',
	'comma': ',',
	'colon': ':',
	'question_mark': '?',
	'exclamation_mark': '!',
	'help':
	{
		# installer
		'install_dependency': 'choose the variant of {dependency} to install',
		'skip_conda': 'skip the conda environment check',
		# general
		'config_path': 'choose the config file to override defaults',
		'source_paths': 'choose single or multiple source images or audios',
		'target_path': 'choose single target image or video',
		'output_path': 'specify the output image or video within a directory',
		'jobs_path': 'specify the directory to store jobs',
		# misc
		'skip_download': 'omit downloads and remote lookups',
		'log_level': 'adjust the message severity displayed in the terminal',
		# execution
		'execution_device_id': 'specify the device used for processing',
		'execution_providers': 'accelerate the model inference using different providers (choices: {choices}, ...)',
		'execution_thread_count': 'specify the amount of parallel threads while processing',
		'execution_queue_count': 'specify the amount of frames each thread is processing',
		# memory
		'video_memory_strategy': 'balance fast frame processing and low VRAM usage',
		'system_memory_limit': 'limit the available RAM that can be used while processing',
		# face analyser
		'face_detector_model': 'choose the model responsible for detecting the faces',
		'face_detector_size': 'specify the size of the frame provided to the face detector',
		'face_detector_angles': 'specify the angles to rotate the frame before detecting faces',
		'face_detector_score': 'filter the detected faces base on the confidence score',
		'face_landmarker_score': 'filter the detected landmarks base on the confidence score',
		# face selector
		'face_selector_mode': 'use reference based tracking or simple matching',
		'face_selector_order': 'specify the order of the detected faces',
		'face_selector_age': 'filter the detected faces based on their age',
		'face_selector_gender': 'filter the detected faces based on their gender',
		'reference_face_position': 'specify the position used to create the reference face',
		'reference_face_distance': 'specify the desired similarity between the reference face and target face',
		'reference_frame_number': 'specify the frame used to create the reference face',
		# face mask
		'face_mask_types': 'mix and match different face mask types (choices: {choices})',
		'face_mask_blur': 'specify the degree of blur applied the box mask',
		'face_mask_padding': 'apply top, right, bottom and left padding to the box mask',
		'face_mask_regions': 'choose the facial features used for the region mask (choices: {choices})',
		# frame extraction
		'trim_frame_start': 'specify the the start frame of the target video',
		'trim_frame_end': 'specify the the end frame of the target video',
		'temp_frame_format': 'specify the temporary resources format',
		'keep_temp': 'keep the temporary resources after processing',
		# output creation
		'output_image_quality': 'specify the image quality which translates to the compression factor',
		'output_image_resolution': 'specify the image output resolution based on the target image',
		'output_audio_encoder': 'specify the encoder used for the audio output',
		'output_video_encoder': 'specify the encoder used for the video output',
		'output_video_preset': 'balance fast video processing and video file size',
		'output_video_quality': 'specify the video quality which translates to the compression factor',
		'output_video_resolution': 'specify the video output resolution based on the target video',
		'output_video_fps': 'specify the video output fps based on the target video',
		'skip_audio': 'omit the audio from the target video',
		# frame processors
		'frame_processors': 'load a single or multiple frame processors. (choices: {choices}, ...)',
		'age_modifier_model': 'choose the model responsible for aging the face',
		'age_modifier_direction': 'specify the direction in which the age should be modified',
		'face_debugger_items': 'load a single or multiple frame processors (choices: {choices})',
		'face_editor_eye_factor': 'specify the eye openness factor',
		'face_editor_eye_blend': 'blend the edited eye into the previous face',
		'face_editor_lip_factor': 'specify the lip openness factor',
		'face_editor_lip_blend': 'blend the edited lip into the previous face',
		'face_enhancer_model': 'choose the model responsible for enhancing the face',
		'face_enhancer_blend': 'blend the enhanced into the previous face',
		'face_swapper_model': 'choose the model responsible for swapping the face',
		'face_swapper_pixel_boost': 'choose the pixel boost resolution for the face swapper',
		'face_swapper_expression_restorer': 'restore expression from target face',
		'frame_colorizer_model': 'choose the model responsible for colorizing the frame',
		'frame_colorizer_blend': 'blend the colorized into the previous frame',
		'frame_colorizer_size': 'specify the size of the frame provided to the frame colorizer',
		'frame_enhancer_model': 'choose the model responsible for enhancing the frame',
		'frame_enhancer_blend': 'blend the enhanced into the previous frame',
		'lip_syncer_model': 'choose the model responsible for syncing the lips',
		# uis
		'open_browser': 'open the browser once the program is ready',
		'ui_layouts': 'launch a single or multiple UI layouts (choices: {choices}, ...)',
		'ui_workflow': 'choose the ui workflow',
		# run
		'run': 'run the program',
		'run_headless': 'run the program in headless mode',
		'force_download': 'force automate downloads and exit',
		# job
		'job_id': 'specify the job id',
		'step_index': 'specify the step index',
		# job manager
		'job_create': 'create a drafted job',
		'job_submit': 'submit a drafted job to become a queued job',
		'job_submit_all': 'submit all drafted jobs to become a queued jobs',
		'job_delete': 'delete a drafted, queued, failed or completed job',
		'job_delete_all': 'delete all drafted, queued, failed and completed jobs',
		'job_list': 'list jobs by status',
		'job_add_step': 'add a step to a drafted job',
		'job_remix_step': 'remix a previous step from a drafted job',
		'job_insert_step': 'insert a step to a drafted job',
		'job_remove_step': 'remove a step from a drafted job',
		# job runner
		'job_run': 'run a queued job',
		'job_run_all': 'run all queued jobs',
		'job_retry': 'retry a failed job',
		'job_retry_all': 'retry all failed jobs'
	},
	'uis':
	{
		# general
		'apply_button': 'APPLY',
		'refresh_button': 'REFRESH',
		'start_button': 'START',
		'stop_button': 'STOP',
		'clear_button': 'CLEAR',
		# about
		'donate_button': 'DONATE',
		# benchmark options
		'benchmark_runs_checkbox_group': 'BENCHMARK RUNS',
		'benchmark_cycles_slider': 'BENCHMARK CYCLES',
		# common options
		'common_options_checkbox_group': 'OPTIONS',
		# execution
		'execution_providers_checkbox_group': 'EXECUTION PROVIDERS',
		# execution queue count
		'execution_queue_count_slider': 'EXECUTION QUEUE COUNT',
		# execution thread count
		'execution_thread_count_slider': 'EXECUTION THREAD COUNT',
		# job manager
		'job_manager_job_action_dropdown': 'JOB_ACTION',
		'job_manager_job_id_dropdown': 'JOB ID',
		'job_manager_step_index_dropdown': 'STEP INDEX',
		# job runner
		'job_runner_job_action_dropdown': 'JOB ACTION',
		'job_runner_job_id_dropdown': 'JOB ID',
		# job list
		'job_list_status_checkbox_group': 'JOB STATUS',
		# face analyser
		'face_detector_model_dropdown': 'FACE DETECTOR MODEL',
		'face_detector_size_dropdown': 'FACE DETECTOR SIZE',
		'face_detector_angles_checkbox_group': 'FACE DETECTOR ANGLES',
		'face_detector_score_slider': 'FACE DETECTOR SCORE',
		'face_landmarker_score_slider': 'FACE LANDMARKER SCORE',
		# face masker
		'face_mask_types_checkbox_group': 'FACE MASK TYPES',
		'face_mask_blur_slider': 'FACE MASK BLUR',
		'face_mask_padding_top_slider': 'FACE MASK PADDING TOP',
		'face_mask_padding_right_slider': 'FACE MASK PADDING RIGHT',
		'face_mask_padding_bottom_slider': 'FACE MASK PADDING BOTTOM',
		'face_mask_padding_left_slider': 'FACE MASK PADDING LEFT',
		'face_mask_region_checkbox_group': 'FACE MASK REGIONS',
		# face selector
		'face_selector_mode_dropdown': 'FACE SELECTOR MODE',
		'face_selector_order_dropdown': 'FACE SELECTOR ORDER',
		'face_selector_age_dropdown': 'FACE SELECTOR AGE',
		'face_selector_gender_dropdown': 'FACE SELECTOR GENDER',
		'reference_face_gallery': 'REFERENCE FACE',
		'reference_face_distance_slider': 'REFERENCE FACE DISTANCE',
		# frame processors
		'frame_processors_checkbox_group': 'FRAME PROCESSORS',
		# frame processors options
		'age_modifier_model_dropdown': 'AGE MODIFIER MODEL',
		'age_modifier_direction_slider': 'AGE MODIFIER DIRECTION',
		'face_debugger_items_checkbox_group': 'FACE DEBUGGER ITEMS',
		'face_editor_eye_factor_slider': 'FACE EDITOR EYE FACTOR',
		'face_editor_eye_blend_slider': 'FACE EDITOR EYE BLEND',
		'face_editor_lip_factor_slider': 'FACE EDITOR LIP FACTOR',
		'face_editor_lip_blend_slider': 'FACE EDITOR LIP BLEND',
		'face_enhancer_model_dropdown': 'FACE ENHANCER MODEL',
		'face_enhancer_blend_slider': 'FACE ENHANCER BLEND',
		'face_swapper_model_dropdown': 'FACE SWAPPER MODEL',
		'face_swapper_pixel_boost_dropdown': 'FACE SWAPPER PIXEL BOOST',
		'face_swapper_expression_restorer_slider': 'FACE SWAPPER EXPRESSION RESTORER',
		'frame_colorizer_model_dropdown': 'FRAME COLORIZER MODEL',
		'frame_colorizer_blend_slider': 'FRAME COLORIZER BLEND',
		'frame_colorizer_size_dropdown': 'FRAME COLORIZER SIZE',
		'frame_enhancer_model_dropdown': 'FRAME ENHANCER MODEL',
		'frame_enhancer_blend_slider': 'FRAME ENHANCER BLEND',
		'lip_syncer_model_dropdown': 'LIP SYNCER MODEL',
		# memory
		'video_memory_strategy_dropdown': 'VIDEO MEMORY STRATEGY',
		'system_memory_limit_slider': 'SYSTEM MEMORY LIMIT',
		# output
		'output_image_or_video': 'OUTPUT',
		# output options
		'output_path_textbox': 'OUTPUT PATH',
		'output_image_quality_slider': 'OUTPUT IMAGE QUALITY',
		'output_image_resolution_dropdown': 'OUTPUT IMAGE RESOLUTION',
		'output_audio_encoder_dropdown': 'OUTPUT AUDIO ENCODER',
		'output_video_encoder_dropdown': 'OUTPUT VIDEO ENCODER',
		'output_video_preset_dropdown': 'OUTPUT VIDEO PRESET',
		'output_video_quality_slider': 'OUTPUT VIDEO QUALITY',
		'output_video_resolution_dropdown': 'OUTPUT VIDEO RESOLUTION',
		'output_video_fps_slider': 'OUTPUT VIDEO FPS',
		# preview
		'preview_image': 'PREVIEW',
		'preview_frame_slider': 'PREVIEW FRAME',
		# source
		'source_file': 'SOURCE',
		# target
		'target_file': 'TARGET',
		# temp frame
		'temp_frame_format_dropdown': 'TEMP FRAME FORMAT',
		# trim frame
		'trim_frame_slider': 'TRIM FRAME',
		# ui workflow
		'ui_workflow': 'UI WORKFLOW',
		# webcam
		'webcam_image': 'WEBCAM',
		# webcam options
		'webcam_mode_radio': 'WEBCAM MODE',
		'webcam_resolution_dropdown': 'WEBCAM RESOLUTION',
		'webcam_fps_slider': 'WEBCAM FPS'
	}
}


def get(key : str) -> Optional[str]:
	if '.' in key:
		section, name = key.split('.')
		if section in WORDING and name in WORDING.get(section):
			return WORDING.get(section).get(name)
	if key in WORDING:
		return WORDING.get(key)
	return None
