from typing import List, Optional
import gradio
import onnxruntime

import facefusion.globals
from facefusion import wording
from facefusion.face_analyser import clear_face_analyser
from facefusion.processors.frame.core import clear_frame_processors_modules
from facefusion.execution import encode_execution_providers, decode_execution_providers

EXECUTION_PROVIDERS_CHECKBOX_GROUP : Optional[gradio.CheckboxGroup] = None


def render() -> None:
	global EXECUTION_PROVIDERS_CHECKBOX_GROUP

	EXECUTION_PROVIDERS_CHECKBOX_GROUP = gradio.CheckboxGroup(
		label = wording.get('uis.execution_providers_checkbox_group'),
		choices = encode_execution_providers(onnxruntime.get_available_providers()),
		value = encode_execution_providers(facefusion.globals.execution_providers)
	)


def listen() -> None:
	EXECUTION_PROVIDERS_CHECKBOX_GROUP.change(update_execution_providers, inputs = EXECUTION_PROVIDERS_CHECKBOX_GROUP, outputs = EXECUTION_PROVIDERS_CHECKBOX_GROUP)


def print_globals():
	# todo pdx 增加配置参数打印
	print("----------------------------------------")
	import inspect
	# 遍历当前模块的全局变量字典
	for name, attr in inspect.getmembers(facefusion.globals, lambda a: not (inspect.isroutine(a))):
		print(f"{name}: {attr}")
	print("----------------------------------------")
def update_execution_providers(execution_providers : List[str]) -> gradio.CheckboxGroup:
	clear_face_analyser()
	clear_frame_processors_modules()
	execution_providers = execution_providers or encode_execution_providers(onnxruntime.get_available_providers())
	facefusion.globals.execution_providers = decode_execution_providers(execution_providers)
	print_globals()
	return gradio.CheckboxGroup(value = execution_providers)
