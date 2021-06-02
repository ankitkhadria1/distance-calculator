import click
from core.get_customers import GetUserDataByDistance

HOME_OFFICE_LAT = "53.339428"
HOME_OFFICE_LONG = "-6.257664"
LINES_PER_SMALL_FILES = 100


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--max_distance",
    default=100,
    prompt="Enter the maximum distance in (KM) from starting point to filter out users, default 100km ",
    help="For ex 100",
)
@click.option(
    "--customers_data_filename",
    default="customers.txt",
    prompt="Enter the name of customers datafile",
    help="For ex customers.txt",
)
def run(max_distance, customers_data_filename):

    """Program to get users based on a one point to another"""
    # Initiate the cls object 
    user_data_obj = GetUserDataByDistance(
        HOME_OFFICE_LAT, HOME_OFFICE_LONG, max_distance, customers_data_filename
    )
    # Break the input file into small chunks
    user_data_obj.break_largefile(lines_per_small_files=10)
    user_data_obj.filter_customers()
    click.echo("...........Saving the data in output.json.....................")


if __name__ == "__main__":
    print("Run python run.py --help to check about command line argument")
    run()
