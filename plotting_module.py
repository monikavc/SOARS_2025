import matplotlib.pyplot as plt
import cartopy.crs as ccrs               
import cartopy.feature as cfeature       
import imageio
import os


def plotting_ozone(data_name, month_index, title, calendar_month, bar_min, bar_max, color, supplemental_info=False):

    plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    data_name[month_index].plot(ax=ax,transform=ccrs.PlateCarree(central_longitude=0), vmin=bar_min, vmax=bar_max, extend='both', cmap=color)
    ax.add_feature(cfeature.COASTLINE, linestyle='--')
    ax.set_global()

    # adding gridlines
    gl = ax.gridlines(draw_labels=True, color='black', alpha=0.5, linestyle='--')
    gl.right_labels = False

    # set title
    ax.set_title(title + ' ' + str(calendar_month[month_index]) + ', 2005-2024', fontsize=14)

    if (supplemental_info==True):
        formatted_mean = f"{data_name[month_index].mean().data:.3f}"
        ax.text(0.10, -0.25, 'Mean: ' + str(formatted_mean) + ' DU', va='bottom', ha='center',
                rotation='horizontal', rotation_mode='anchor',
                transform=ax.transAxes, fontsize=12)

    plt.show()


def plotting_ozone_contourf(lon, lat, data_name, month_index, title, calendar_month, bar_min, bar_max, supplemental_info=False):

    plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    cf = plt.contourf(lon,lat,data_name[month_index],transform=ccrs.PlateCarree(central_longitude=0), cmap='rainbow', extend='both', vmin=bar_min, vmax=bar_max)
    ax.add_feature(cfeature.COASTLINE, linestyle='--')
    ax.set_global()

    # adding gridlines
    gl = ax.gridlines(draw_labels=True, color='black', alpha=0.5, linestyle='--')
    gl.right_labels = False

    # set title
    ax.set_title(title + ' ' + str(calendar_month[month_index]) + ', 2005-2024', fontsize=14)

    if (supplemental_info==True):
        formatted_mean = f"{data_name[month_index].mean().data:.3f}"
        ax.text(0.10, -0.25, 'Mean: ' + str(formatted_mean) + ' DU', va='bottom', ha='center',
                rotation='horizontal', rotation_mode='anchor',
                transform=ax.transAxes, fontsize=12)
    plt.colorbar(cf, shrink=0.8, pad=0.07)

    plt.show()


def create_gif(image_folder, output_gif, duration, filename):
    filenames = sorted([f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))])
    images = []
    for filename in filenames:
        if filename.startswith(filename):
            image_path = os.path.join(image_folder, filename)
            images.append(imageio.imread(image_path))
    imageio.mimsave(output_gif, images, duration=duration)