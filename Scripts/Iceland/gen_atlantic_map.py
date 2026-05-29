"""
gen_atlantic_map.py
Generate a clean North Atlantic map showing USA - Atlantic Ocean - Europe.
White background, light grey land, clean country borders.
Saves to Output/Iceland/maps/north_atlantic_wide.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from pathlib import Path

OUT = Path(r"C:\Users\parth.pandya\Projects\YouTube\Output\Iceland\maps\north_atlantic_wide.png")

# 1920x1080 at 96 dpi
fig = plt.figure(figsize=(20, 11.25), dpi=96)
fig.patch.set_facecolor("white")

proj = ccrs.PlateCarree()
ax = fig.add_axes([0, 0, 1, 1], projection=proj)

# Extent: USA east coast to western Europe, enough latitude for Iceland
ax.set_extent([-100, 30, 20, 75], crs=ccrs.PlateCarree())

# Ocean — light blue-grey
ax.set_facecolor("#D6E8F5")

# Land — warm light grey
land = cfeature.NaturalEarthFeature(
    "physical", "land", "50m",
    facecolor="#E8E4DC", edgecolor="#AAAAAA", linewidth=0.8
)
ax.add_feature(land)

# Country borders
borders = cfeature.NaturalEarthFeature(
    "cultural", "admin_0_countries", "50m",
    facecolor="none", edgecolor="#888888", linewidth=0.6
)
ax.add_feature(borders)

# US State lines (subtle)
states = cfeature.NaturalEarthFeature(
    "cultural", "admin_1_states_provinces_lines", "50m",
    facecolor="none", edgecolor="#BBBBBB", linewidth=0.4
)
ax.add_feature(states)

# Gridlines — very faint
gl = ax.gridlines(draw_labels=False, linewidth=0.3,
                  color="#CCCCCC", alpha=0.7, linestyle="--")

plt.savefig(str(OUT), dpi=96, bbox_inches="tight",
            facecolor="white", pad_inches=0)
plt.close()

size_kb = OUT.stat().st_size // 1024
print(f"Saved: {OUT.name}  ({size_kb} KB)")
print(f"Path:  {OUT}")
