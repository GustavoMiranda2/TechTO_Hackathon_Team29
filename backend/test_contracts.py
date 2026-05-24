import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProductContractTests(unittest.TestCase):
    def test_signup_collects_only_credentials(self):
        tree = ast.parse((ROOT / "backend" / "main.py").read_text())
        signup = next(
            n
            for n in tree.body
            if isinstance(n, ast.ClassDef) and n.name == "SignupRequest"
        )
        field_names = {n.target.id for n in signup.body if isinstance(n, ast.AnnAssign)}
        self.assertEqual(field_names, {"username", "password"})
        self.assertEqual(
            [b.id for b in signup.bases if isinstance(b, ast.Name)], ["BaseModel"]
        )

    def test_auth_ui_does_not_collect_questionnaire_fields(self):
        auth = (ROOT / "frontend" / "app" / "components" / "Auth.tsx").read_text()
        removed_copy = [
            "Where are you right now?",
            "Experience level",
            "Skills",
            "Interests",
            "Your goals",
            "Roles you're curious about",
        ]
        for text in removed_copy:
            self.assertNotIn(text, auth)

    def test_agent_has_internal_discovery_skills(self):
        agent_source = (ROOT / "backend" / "agent.py").read_text()
        self.assertIn("INTERNAL DISCOVERY SKILLS", agent_source)
        self.assertIn("do not ask these items as a checklist", agent_source)
        self.assertIn("The person can choose more than one option", agent_source)

    def test_diagnosis_contract_includes_saved_preferences(self):
        agent_source = (ROOT / "backend" / "agent.py").read_text()
        main_source = (ROOT / "backend" / "main.py").read_text()
        self.assertIn('"inferred_profile"', agent_source)
        self.assertIn("save_inferred_profile", main_source)


if __name__ == "__main__":
    unittest.main()
