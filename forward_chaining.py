import tkinter as tk
from tkinter import scrolledtext

def forward_chaining(initial_facts, rules):
    facts = initial_facts.copy()
    new_facts = []

    while True:
        newly_derived_facts = []

        for rule in rules:
            premise, conclusion = rule
            if all(cond in facts for cond in premise.split(' and ')) and conclusion not in facts:
                newly_derived_facts.append(conclusion)
                facts.append(conclusion)

        new_facts.extend(newly_derived_facts)

        if not newly_derived_facts:
            break

    return facts, new_facts

class ForwardChainingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Forward Chaining System")

        self.facts = []
        self.rules = []

        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.root, width=60, height=20, font=("Helvetica", 12))
        self.text_area.pack(padx=10, pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.btn_add_facts = tk.Button(btn_frame, text="Add Facts", command=self.add_facts)
        self.btn_add_facts.pack(side=tk.LEFT, padx=5)

        self.btn_add_rules = tk.Button(btn_frame, text="Add Rules", command=self.add_rules)
        self.btn_add_rules.pack(side=tk.LEFT, padx=5)

        self.btn_generate_facts = tk.Button(btn_frame, text="Generate Facts", command=self.generate_facts)
        self.btn_generate_facts.pack(side=tk.LEFT, padx=5)

        self.btn_exit = tk.Button(btn_frame, text="Exit", command=self.root.destroy)
        self.btn_exit.pack(side=tk.LEFT, padx=5)

    def add_facts(self):
        facts_window = tk.Toplevel(self.root)
        facts_window.title("Add Facts")

        label = tk.Label(facts_window, text="Enter facts (press Enter to finish):")
        label.pack(padx=10, pady=5)

        entry = tk.Entry(facts_window, font=("Helvetica", 12))
        entry.pack(padx=30, pady=5)

        entry.focus_set()

        def add_fact():
            fact = entry.get().strip()
            if fact:
                self.facts.append(fact)
                self.update_text_area()
            entry.delete(0, tk.END)

        entry.bind("<Return>", lambda event: add_fact())

    def add_rules(self):
        rules_window = tk.Toplevel(self.root)
        rules_window.title("Add Rules")

        label = tk.Label(rules_window, text="Enter rule (e.g., A and B, C):")
        label.pack(padx=10, pady=5)

        entry = tk.Entry(rules_window, font=("Helvetica", 12))
        entry.pack(padx=30, pady=5)

        entry.focus_set()

        def add_rule():
            rule_input = entry.get().strip()
            if rule_input:
                self.rules.append(tuple(rule_input.split(', ')))
                self.update_text_area()
            entry.delete(0, tk.END)

        entry.bind("<Return>", lambda event: add_rule())

    def generate_facts(self):
        facts, new_facts = forward_chaining(self.facts, self.rules)
        result = f"\nFacts: {', '.join(facts)}\nNew Facts: {', '.join(new_facts)}"
        self.text_area.insert(tk.END, result)

    def update_text_area(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Facts:\n{', '.join(self.facts)}\n\nRules:\n")
        for rule in self.rules:
            self.text_area.insert(tk.END, f"{', '.join(rule)}\n")
        self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ForwardChainingGUI(root)
    root.mainloop()
