import pandas as pd
import sys

def display_row_in_markdown(df, workshop_name):
    # Check if the workshop exists in the DataFrame
    filtered_df = df[df['Workshop'] == workshop_name]
    if filtered_df.empty:
        # Return a placeholder message if the workshop is not found
        return f"# {workshop_name} Workshop\n\n**Details of this course will be confirmed soon!**\n"

    # Retrieve the first row of the filtered DataFrame
    row_data = filtered_df.iloc[0]

    # Determine the next session date using either 'NextSession' or 'VerboseNextSession'
    if pd.isna(row_data['NextSession']):
        next_session = row_data['VerboseNextSession'] if pd.notna(row_data['VerboseNextSession']) else "TBD"
    else:
        next_session = row_data['NextSession']

    # Start constructing the Markdown content with a header and session information
    markdown_output = f"# Welcome to the {row_data['Workshop']} Workshop\n"
    markdown_output += f"**Next Session Date:** {next_session}\n\n"
    markdown_output += f"**What to Expect:**\n{row_data['Overview']}\n\n"

    # Explain whether registration is currently open or closed in a full sentence
    if row_data['RegistrationLive'] == 'Y':
        registration_status = "Registration is currently open."
    else:
        registration_status = "Registration is currently closed."
    markdown_output += f"**Registration Status:** {registration_status}\n"
    
    # Provide registration closing date in a friendly format
    markdown_output += f"**Please register by:** {row_data['ClosingDate'] if pd.notna(row_data['ClosingDate']) else 'No deadline specified'}\n"
    markdown_output += f"**Installation Instructions:** [Click here to install]({row_data['InstallationLink']})\n"

    return markdown_output

def main():
    # Verify the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: Please run the script as follows: python script.py <path_to_csv> <workshop_name> <output_markdown_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    workshop_name = sys.argv[2]
    output_md_path = sys.argv[3]

    # Load the workshop details from the provided CSV file
    df = pd.read_csv(csv_file_path)

    # Generate Markdown content for the specified workshop
    markdown_content = display_row_in_markdown(df, workshop_name)

    # Write the generated Markdown content to the specified output file
    with open(output_md_path, 'w') as f:
        f.write(markdown_content)

    print(f"The markdown file has been successfully created and saved to {output_md_path}.")

if __name__ == "__main__":
    main()
