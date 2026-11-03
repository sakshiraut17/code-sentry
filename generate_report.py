
pdf.chapter_title("5. Clarity of the README and stated assumptions")
pdf.chapter_body("The README.md provides crystal-clear setup instructions (including required pip installs and environment variables), execution commands for both the app and the unit test suite, and a full sample input/output demonstration. It clearly states the assumptions made, such as relying on the newest google-genai SDK's Chat API for function calling and the addition of the retry mechanism.")

pdf.chapter_title("6. Deliverables Provided")
pdf.chapter_body(
    "- Source code repository: The complete source code is bundled within the 'code_sentry' directory, ready to be initialized as a Git repository or compressed into a zipped folder for final submission.\n"
    "- README.md: A comprehensive README is included at the project root. It explicitly covers the prerequisites, setup instructions, execution commands, a full example of input/output, and stated assumptions.\n"
    "- Short Demo: A self-contained demo is built directly into main.py. Running 'python main.py' automatically submits a sample code snippet (containing command injection and weak hashing vulnerabilities) along with a natural language query. This showcases the end-to-end AI-powered analysis. The output of this demo is also documented inside the README."
)

pdf.output("Evaluation_Report.pdf")
print("PDF generated successfully.")
