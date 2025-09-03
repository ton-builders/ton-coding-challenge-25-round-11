const { Telegraf } = require('telegraf');
const { getAvailableGifts } = require('./getAvailableGifts');

const bot = new Telegraf(process.env.BOT_TOKEN);

function formatGift(gift, index) {
  const emoji = gift.sticker?.emoji || '🎁';
  const base = `${emoji} ${gift.star_count}⭐`;
  return gift.remaining_count !== undefined && gift.total_count !== undefined
    ? `${index + 1}. ${base} 可升级`
    : `${index + 1}. ${base}`;
}

bot.command('gifts', async (ctx) => {
  try {
    const gifts = await getAvailableGifts();
    if (!gifts || gifts.length === 0) {
      return ctx.reply('No gifts available');
    }
    const text = gifts.map(formatGift).join('\n');
    ctx.reply(text);
  } catch {
    ctx.reply('Error while getting gifts');
  }
});

bot.launch();

process.once('SIGINT', () => bot.stop());
process.once('SIGTERM', () => bot.stop());
