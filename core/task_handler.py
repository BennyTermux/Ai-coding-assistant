import uuid
from ai.provider_router import AIProviderRouter
from core.file_manager import FileManager
from github.github_manager import GitHubManager

class TaskHandler:

    @staticmethod
    def handle_prompt(prompt: str):
        project_name = f"project_{uuid.uuid4().hex[:6]}"
        project_path = FileManager.create_project(project_name)

        ai_response = AIProviderRouter.generate(
            f"Create a full project with files. Return JSON with filenames and contents.\n\n{prompt}"
        )

        # NOTE: In production, parse JSON safely
        FileManager.write_file(project_path, "output.txt", ai_response)

        repo_url = GitHubManager.create_and_push(project_name, project_path)

        return {
            "project": project_name,
            "path": project_path,
            "repo": repo_url,
            "summary": ai_response[:500]
        }
