from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load CPI data (assuming cpi_data.csv is in the same directory)
try:
    cpi_df = pd.read_csv('cpi_data.csv')
    cpi_df['Date'] = pd.to_datetime(cpi_df['Date'], format='%Y-%m') # Parse Date column
    cpi_df.set_index('Date', inplace=True) # Set Date as index for efficient lookup
except FileNotFoundError:
    cpi_df = None # Handle the case where the CSV is not found

def get_cpi_for_date(date_str):
    """Retrieves CPI value for a given date (YYYY-MM)."""
    if cpi_df is None:
        return None, "CPI data file not found."
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m')
        cpi_value = cpi_df.loc[date_obj, 'CPI']
        return cpi_value, None
    except KeyError:
        return None, "Seçilen tarih için TÜFE verisi bulunamadı." # Turkish error message
    except ValueError:
        return None, "Geçersiz tarih formatı. Lütfen YYYY-MM formatını kullanın." # Turkish error message

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    start_date_str = None
    end_date_str = None
    cpi_change_percent = None
    value_at_end = None
    lira_amount = 100 # Default amount

    if request.method == 'POST':
        start_month = request.form['start_month']
        start_year = request.form['start_year']
        end_month = request.form['end_month']
        end_year = request.form['end_year']
        try:
            lira_amount = float(request.form['lira_amount']) # Get user entered amount
        except ValueError:
            lira_amount = 100 # Default to 100 if input is invalid

        start_date_str = f"{start_year}-{start_month.zfill(2)}"
        end_date_str = f"{end_year}-{end_month.zfill(2)}"

        start_cpi, start_error = get_cpi_for_date(start_date_str)
        end_cpi, end_error = get_cpi_for_date(end_date_str)

        if start_error or end_error:
            error_message = start_error or end_error
            error = error_message
        elif start_cpi is not None and end_cpi is not None:
            cpi_change_percent = ((end_cpi - start_cpi) / start_cpi) * 100
            value_at_end = lira_amount * (end_cpi / start_cpi) # Corrected calculation
        else:
             error = "Seçilen tarihlerden biri veya her ikisi için TÜFE verisi alınamadı." # Turkish error

    months = [("01", "Ocak"), ("02", "Şubat"), ("03", "Mart"), ("04", "Nisan"), # Turkish months
              ("05", "Mayıs"), ("06", "Haziran"), ("07", "Temmuz"), ("08", "Ağustos"),
              ("09", "Eylül"), ("10", "Ekim"), ("11", "Kasım"), ("12", "Aralık")]
    current_year = datetime.now().year
    years = list(range(1978, current_year + 1))

    return render_template('index.html',
                           months=months,
                           years=years,
                           error=error,
                           start_date=start_date_str,
                           end_date=end_date_str,
                           cpi_change_percent=cpi_change_percent,
                           value_at_end=value_at_end,
                           lira_amount=lira_amount) # Pass lira_amount to template

if __name__ == '__main__':
    app.run(debug=True)
