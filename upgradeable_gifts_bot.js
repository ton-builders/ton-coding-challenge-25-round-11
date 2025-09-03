const { Telegraf } = require('telegraf');
const { getAvailableGifts } = require('./getAvailableGifts');

const bot = new Telegraf(process.env.BOT_TOKEN);

function isUpgradeable(gift) {
  return gift.remaining_count !== undefined && gift.total_count !== undefined;
}

bot.command('gifts', async (ctx) => {
  try {
    const gifts = await getAvailableGifts();
    if (!gifts?.length) return ctx.reply('No gifts available');

    const text = gifts.map(g => {
      const emoji = g.sticker?.emoji || '🎁';
      return `${emoji} ${g.star_count}⭐${isUpgradeable(g) ? ' 可升级' : ''}`;
    }).join('\n');

    ctx.reply(text);
  } catch {
    ctx.reply('Error while getting gifts');
  }
});

bot.launch();

process.once('SIGINT', () => bot.stop());
process.once('SIGTERM', () => bot.stop());
