import { readFileSync } from 'fs';
import * as yaml from 'js-yaml';
import { join } from 'path';
import { AppConfigType } from './config.type';

const CONFIG_FILENAME = (isDev: boolean) => {
  if (isDev) {
    return 'dev.config.yaml';
  }

  return 'config.prod.yaml';
}

export default function loadAppConfig() {
  try {
    const path = join(process.cwd(), CONFIG_FILENAME(true));
    const cfg = yaml.load(
      readFileSync(path, 'utf-8')
    ) as AppConfigType;
    return cfg;
  } catch (error) {
    throw error;
  }
}