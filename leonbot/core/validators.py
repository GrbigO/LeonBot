from os.path import join, exists


def validate_ai_paths(ai_output_folder_path, *args):
	if not exists(ai_output_folder_path):
		raise FileNotFoundError(f"AI model folder does not exist at {ai_output_folder_path}")

	for arg in args:
		path = join(arg)
		if not exists(path):
			FileNotFoundError(f"not valid path {path}")