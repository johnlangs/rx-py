wget https://dailymed-data.nlm.nih.gov/public-release-files/dm_spl_monthly_update_aug2023.zip
find . -iname '*.zip' -exec sh -c 'unzip -o -d "${0%.*}" "$0"' '{}' ';'
cd dm_spl_monthly_update_aug2023/
find . -iname '*.zip' -exec sh -c 'unzip -o -d "${0%.*}" "$0"' '{}' ';'
cd prescription/
rm *.zip
cd otc/
rm *.zip