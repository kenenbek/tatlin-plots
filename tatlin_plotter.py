import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings

warnings.filterwarnings("ignore")
sns.set(style="darkgrid")

def json_file_reader(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def preprocess_history(history):
    for h in history:
        storage_components = {}
        for storage_component in h['storage_components']:
            storage_components[storage_component['name']] = storage_component
        h['storage_components'] = storage_components
    return history


def _subplotter(w_data_old, w_data_new, r_data_old, r_data_new, name):
    fig, ax_list = plt.subplots(2, 2, figsize=(15,6))
    fig.style
    
    ax_list[0, 0].plot(w_data_old, lw=3, c='b')
    ax_list[0, 1].plot(w_data_new, lw=3, c='r')
    ax_list[1, 0].plot(r_data_old, lw=3, c='b')
    ax_list[1, 1].plot(r_data_new, lw=3, c='r')
    
    ax_list[0, 0].title.set_text("Run11")
    ax_list[0, 0].title.set_size(15)
    ax_list[0, 1].title.set_text("Run11X")
    ax_list[0, 1].title.set_size(15)
    
    fig.suptitle(name.upper(), size=18)
    fig.text(0.093, 0.74, 'Write', rotation=90, fontsize=15)
    fig.text(0.093, 0.34, 'Read', rotation=90, fontsize=15)
    fig.show()


def plot_history(w_history_old, w_history_new, r_history_old, r_history_new):
    ATM_NAMES = ['air_temp', 'humidity', 'atm_pressure', 'vibration']
    
    for name in ATM_NAMES:
        w_data_old = [h['ambience'][name] for h in w_history_old]
        w_data_new = [h['ambience'][name] for h in w_history_new]
        r_data_old = [h['ambience'][name] for h in r_history_old]
        r_data_new = [h['ambience'][name] for h in r_history_new]
    
        _subplotter(w_data_old, w_data_new, r_data_old, r_data_new, name)
    
    return 
    storage_states = list(w_history_old[0]['storage_state'].keys())
    for storage_state in storage_states:
        w_statistics_old = [h['storage_state'][storage_state] for h in w_history_old]
        w_statistics_new = [h['storage_state'][storage_state] for h in w_history_new]
        
        r_statistics_old = [h['storage_state'][storage_state] for h in r_history_old]
        r_statistics_new = [h['storage_state'][storage_state] for h in r_history_new]
        
        _subplotter(w_statistics_old, w_statistics_new, r_statistics_old, r_statistics_new, '{}'.format(storage_state))
        
    
    storage_components_props_pairs = []
    
    for _, storage_component in w_history_old[0]['storage_components'].items():
        for prop in storage_component['props']:
            storage_components_props_pairs.append((storage_component['name'], prop))
    
    for storage_component, prop in storage_components_props_pairs:
        w_statistics_old = [h['storage_components'][storage_component]['props'][prop] for h in w_history_old]
        w_statistics_new = [h['storage_components'][storage_component]['props'][prop] for h in w_history_new]
        
        r_statistics_old = [h['storage_components'][storage_component]['props'][prop] for h in r_history_old]
        r_statistics_new = [h['storage_components'][storage_component]['props'][prop] for h in r_history_new]
        _subplotter(w_statistics_old, w_statistics_new, r_statistics_old, r_statistics_new, '{} {}'.format(storage_component, prop))