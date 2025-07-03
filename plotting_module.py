import matplotlib.pyplot as plt
import cartopy.crs as ccrs               
import cartopy.feature as cfeature       

def plotting_ozone(data_name, month_index, title, calendar_month, years, bar_min, bar_max, supplemental_info=False):

    plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    data_name[month_index].plot(ax=ax,transform=ccrs.PlateCarree(central_longitude=0), vmin=bar_min, vmax=bar_max, extend='both')
    ax.add_feature(cfeature.COASTLINE, linestyle='--')
    ax.set_global()

    # adding gridlines
    ax.gridlines(draw_labels=True, color='black', alpha=0.5, linestyle='--')

    ax.set_title(title + ' ' + calendar_month + ', 2005-2024', fontsize=14)

    if (supplemental_info==True):
        formatted_mean = f"{data_name[month_index].mean().data:.3f}"
        ax.text(0.10, -0.25, 'Mean: ' + str(formatted_mean) + ' DU', va='bottom', ha='center',
                rotation='horizontal', rotation_mode='anchor',
                transform=ax.transAxes, fontsize=12)

    plt.show()