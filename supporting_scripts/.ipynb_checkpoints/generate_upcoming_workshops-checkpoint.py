import pandas as pd
import sys
from datetime import datetime, timedelta

def parse_dates(date_str):
    try:
        return datetime.strptime(date_str.split(',')[0].strip(), '%d/%m/%Y')
    except:
        return None

def display_workshops_in_markdown(df, filter_next_month=False):
    now = datetime.now()
    one_month_later = now + timedelta(days=30)
    
    markdown_output = ""
    for _, row in df.iterrows():
        parsed_date = row['ParsedDate']
        
        # If filter for the next month is active and the workshop date doesn't fit the criteria, skip it
        if filter_next_month:
            if parsed_date is None or parsed_date > one_month_later or parsed_date < now:
                continue

        next_session = row['NextSession'] if pd.notna(row['NextSession']) else row['VerboseNextSession'] if pd.notna(row['VerboseNextSession']) else "TBD"
        markdown_output += f"# Welcome to the {row['Workshop']} Workshop\n"
        markdown_output += f"**Next Session Date:** {next_session}\n\n"
        markdown_output += f"**What to Expect:**\n{row['Overview']}\n\n"
        registration_status = "Registration is currently open." if row['RegistrationLive'] == 'Y' else "Registration is currently closed."
        markdown_output += f"**Registration Status:** {registration_status}\n"
        closing_date = row['ClosingDate'] if pd.notna(row['ClosingDate']) else 'No deadline specified'
        markdown_output += f"**Please register by:** {closing_date}\n"
        markdown_output += f"**Installation Instructions:** [Click here to install]({row['InstallationLink']})\n\n"
        
        # Add a horizontal line separator between workshops
        markdown_output += "---\n\n"
    
    return markdown_output

def main():
    if len(sys.argv) != 4:
        print("Usage: Please run the script as follows: python script.py <path_to_csv> <output_markdown_all_path> <output_markdown_next_month_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    output_md_all_path = sys.argv[2]
    output_md_next_month_path = sys.argv[3]

    # Load the workshop details from the provided CSV file
    df = pd.read_csv(csv_file_path)
    df['ParsedDate'] = df['NextSession'].apply(parse_dates)
    df = df.sort_values(by='ParsedDate', ascending=True, na_position='last')

    # Generate Markdown content for all workshops
    markdown_all = display_workshops_in_markdown(df)
    # Generate Markdown content for workshops in the next month
    markdown_next_month = display_workshops_in_markdown(df, filter_next_month=True)

    # Write the generated Markdown content to the specified output files
    with open(output_md_all_path, 'w') as f:
        f.write(markdown_all)
    with open(output_md_next_month_path, 'w') as f:
        f.write(markdown_next_month)

    print(f"The markdown files have been successfully created and saved to {output_md_all_path} and {output_md_next_month_path}.")

if __name__ == "__main__":
    main()
