# ...existing code...
import subprocess

def check_git_version():
	try:
		out = subprocess.check_output(["git", "--version"], text=True, stderr=subprocess.STDOUT)
		print(out.strip())
		return True
	except FileNotFoundError:
		print("Git is not installed or not found in PATH.")
		return False
	except subprocess.CalledProcessError as e:
		print("Error running git:", e.output if hasattr(e, 'output') else e)
		return False


if __name__ == '__main__':
	check_git_version()

# ...existing code...