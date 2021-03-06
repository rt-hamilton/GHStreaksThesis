# ---------- IMPORT ------------
import logging
import datetime
import json
# ------------------------------


# ---------- INPUT -------------
path_source = ""
# ------------------------------


# ---------- OUTPUT ------------
path_results = ""
# ------------------------------


# ---------- CONFIG ------------

# ------------------------------


# ---------- INITIAL -----------
logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
datetimeFormat = "%Y-%m-%d"
# ------------------------------



log_starttime = datetime.datetime.now()

# CODE

log_endtime = datetime.datetime.now()
log_runtime = (log_endtime - log_starttime)
logging.info("Total runtime: " + str(log_runtime))