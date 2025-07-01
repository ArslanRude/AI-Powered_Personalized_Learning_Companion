import json

class MemoryModule:
    def __init__(self):
        self.progress = {}

    def track_progress(self, student_id, topic, progress):
        try:
            if student_id not in self.progress:
                self.progress[student_id] = {}
            self.progress[student_id][topic] = progress
            self.save_progress()
            return True
        except Exception as e:
            return f"Error tracking progress: {str(e)}"

    def get_progress(self, student_id, topic=None):
        try:
            if student_id not in self.progress:
                return "No progress found for this student"
            if topic:
                return self.progress[student_id].get(topic, "No progress found for this topic")
            return self.progress[student_id]
        except Exception as e:
            return f"Error getting progress: {str(e)}"

    def save_progress(self):
        try:
            with open("progress.json", "w") as f:
                json.dump(self.progress, f)
            return True
        except Exception as e:
            return f"Error saving progress: {str(e)}"